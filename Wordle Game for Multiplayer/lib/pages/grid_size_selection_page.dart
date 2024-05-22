import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:yazlab2_2/providers/controller.dart';
import 'package:yazlab2_2/services/auth_service.dart';
import 'package:yazlab2_2/services/database_service.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'channel_page.dart';

class GridSizeSelectionPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final controller = Provider.of<Controller>(context);
    final authService = Provider.of<AuthService>(context, listen: false);
    final dbService = DatabaseService();

    return Scaffold(
      appBar: AppBar(title: Center(child: Text('Grid Boyutu Seçimi'))),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: List.generate(4, (index) {
            int gridSize = 4 + index;  // 4x6, 5x6, 6x6, 7x6
            String channelId = "$gridSize" + "x6"; 
            return ElevatedButton(
              child: Text('$gridSize x 6 Grid'),
              onPressed: () async {
                await dbService.joinOrCreateChannel('$gridSize x 6', channelId);
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => ChannelPage(gridSize: '$gridSize x 6', channelId: channelId),
                  ),
                );
              },
            );
          }),
        ),
      ),
    );
  }
}
