import 'dart:async';

import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:yazlab2_2/pages/word_entry_screen.dart';
import 'package:yazlab2_2/services/database_service.dart';

class ChannelPage extends StatefulWidget {
  final String gridSize;
  final String channelId;

  ChannelPage({Key? key, required this.gridSize, required this.channelId})
      : super(key: key);

  @override
  _ChannelPageState createState() => _ChannelPageState();
}

class _ChannelPageState extends State<ChannelPage> {
  final DatabaseService _dbService = DatabaseService();
  Stream<DatabaseEvent>? _channelStream;
  StreamSubscription<DatabaseEvent>? _invitesSubscription;

  @override
  void initState() {
    super.initState();
    _channelStream = _dbService.listenToChannel(
        widget.gridSize.replaceFirst(' x ', 'x'), widget.channelId);
    print(widget.gridSize);

    int columnCount = int.parse(widget.gridSize.split(' x ')[0]);
    print(columnCount);

    _invitesSubscription = _dbService
        .listenToInvites(FirebaseAuth.instance.currentUser!.uid)
        .listen((DatabaseEvent event) {
      final value = event.snapshot.value;
      if (value != null && value is Map) {
        Map<dynamic, dynamic> data = value;
        data.forEach((key, value) {
          if (value['status'] == 'pending') {
            String inviteId = key; // Davetin benzersiz ID'sini alıyoruz
            String message = "Davet: ${value['invitingUserId']} - Durum: ${value['status']}";
            showInviteResponseDialog(context, message, inviteId, columnCount);
          }
        });
      }
    });
  }

  @override
  void dispose() {
    _invitesSubscription?.cancel();
    _dbService.removeUserFromChannel(
        widget.channelId, FirebaseAuth.instance.currentUser!.uid);
    super.dispose();
  }

  void showInviteResponseDialog(
      BuildContext context, String message, String inviteId, int columnCount) {
    showDialog(
      context: context,
      builder: (BuildContext dialogContext) {
        return AlertDialog(
          title: Text('Davet Durumu'),
          content: Text(message),
          actions: <Widget>[
            TextButton(
              child: Text('Kabul Et'),
              onPressed: () async {
                await _dbService.acceptInvite(inviteId);
                Navigator.of(dialogContext).pop(); 

                
                Navigator.of(context).pushReplacement(
                  
                  MaterialPageRoute(
                      builder: (context) =>
                          WordEntryScreen(columnCount: columnCount)),
                );
              },
            ),
            TextButton(
              child: Text('Reddet'),
              onPressed: () {
                _dbService.rejectInvite(inviteId);
                Navigator.of(dialogContext).pop(); 
              },
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Channel: ${widget.gridSize}"),
        actions: <Widget>[
          IconButton(
            icon: Icon(Icons.notifications),
            onPressed: () => _showInvites(context),
          )
        ],
      ),
      body: StreamBuilder<DatabaseEvent>(
        stream: _channelStream,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          }
          if (!snapshot.hasData || snapshot.data!.snapshot.value == null) {
            return Center(child: Text("No data available"));
          }
          var channelData = snapshot.data!.snapshot.value;
          if (channelData is! Map) {
            return Center(child: Text("Data format error"));
          }
          Map<String, dynamic> channelMap =
              Map<String, dynamic>.from(channelData);
          return _buildPlayerList(channelMap['players'] ?? {});
        },
      ),
    );
  }

  Widget _buildPlayerList(Map<dynamic, dynamic> playersMap) {
    Map<String, dynamic> safePlayersMap = {};
    playersMap.forEach((key, value) {
      if (key is String && value is Map) {
        safePlayersMap[key] = Map<String, dynamic>.from(value);
      }
    });

    // ...

    List<Widget> players = safePlayersMap.entries.map((entry) {
      Map<String, dynamic> playerInfo = entry.value;
      bool isCurrentUser = entry.key == FirebaseAuth.instance.currentUser!.uid;
      return ListTile(
        title: Text("${playerInfo['username']} - ${playerInfo['status']}"),
        trailing: !isCurrentUser
            ? ElevatedButton(
                child: Text("Duello Daveti"),
                onPressed: () => _sendInvite(entry.key),
              )
            : null,
      );
    }).toList();

    return ListView(children: players);
  }

  void _sendInvite(String invitedUserId) {
    String? currentUserId = FirebaseAuth.instance.currentUser?.uid;
    int columnCount = int.parse(widget.gridSize.split(' x ')[0]);
    if (currentUserId != null && invitedUserId != currentUserId) {
      _dbService
          .sendInvite(widget.channelId, currentUserId, invitedUserId, columnCount)
          .then((_) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text("Davet gönderildi")),
        );
      }).catchError((error) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
              content: Text("Davet gönderilirken bir hata oluştu: $error")),
        );
      });
    }
  }

  void _showInvites(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Davetler'),
          content: Container(
            width: double.maxFinite,
            child: StreamBuilder<DatabaseEvent>(
              stream: _dbService
                  .listenToInvites(FirebaseAuth.instance.currentUser!.uid)
                  .asBroadcastStream(),
              builder: (context, snapshot) {
                if (snapshot.connectionState == ConnectionState.waiting) {
                  return Center(child: CircularProgressIndicator());
                }
                if (!snapshot.hasData ||
                    snapshot.data!.snapshot.value == null) {
                  return Center(child: Text("No data available"));
                }
                var invitesData = snapshot.data!.snapshot.value;
                if (invitesData is! Map) {
                  return Center(child: Text("Data format error"));
                }
                Map<String, dynamic> invitesMap =
                    Map<String, dynamic>.from(invitesData);
                return ListView(
                  children: invitesMap.entries.map((entry) {
                    Map<String, dynamic> inviteInfo =
                        Map<String, dynamic>.from(entry.value);
                    int columnCount =
                        int.parse(inviteInfo['gridSize'].split(' ')[0]);
                    return ListTile(
                      title: Text("Davet: ${inviteInfo['invitingUserId']}"),
                      subtitle: Text("Durum: ${inviteInfo['status']}"),
                      onTap: () {
                        
                        _dbService.acceptInvite(entry.key.toString());
                        print("Yönlendirme yapılıyor...");
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                              builder: (context) =>
                                  WordEntryScreen(columnCount: columnCount)),
                        );
                        Navigator.of(context).pop();
                      },
                    );
                  }).toList(),
                );
              },
            ),
          ),
          actions: <Widget>[
            TextButton(
              child: Text('Kapat'),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      },
    );
  }
}
