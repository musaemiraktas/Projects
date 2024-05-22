import 'dart:async';
import 'package:flutter/material.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:yazlab2_2/services/database_service.dart';
import 'package:yazlab2_2/pages/word_entry_screen.dart';  // Yönlendirme yapılacak ekranın importu

class InviteStatusListener extends StatefulWidget {
  final String inviteId;

  const InviteStatusListener({Key? key, required this.inviteId}) : super(key: key);

  @override
  _InviteStatusListenerState createState() => _InviteStatusListenerState();
}

class _InviteStatusListenerState extends State<InviteStatusListener> {
  late StreamSubscription inviteStatusSubscription;
  int? columnCount;

  @override
  void initState() {
    super.initState();
    inviteStatusSubscription = DatabaseService().listenToSpecificInvite(widget.inviteId).listen((event) {
      final data = event.snapshot.value as Map?;
      if (data != null) {
        setState(() {
          columnCount = int.tryParse(data['gridSize'].split('x')[0].trim());
        });
        if (data['status'] == 'accepted' && columnCount != null) {
          Navigator.of(context).pushReplacement(
            MaterialPageRoute(
              builder: (context) => WordEntryScreen(columnCount: columnCount!),
            ),
          );
        }
      }
    });
  }

  @override
  void dispose() {
    inviteStatusSubscription.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Davet Durumu"),
      ),
      body: Center(child: Text("Davet durumu bekleniyor...")),
    );
  }
}
