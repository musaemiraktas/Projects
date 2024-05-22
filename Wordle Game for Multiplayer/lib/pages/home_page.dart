import 'dart:math';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:provider/provider.dart';
import 'package:yazlab2_2/components/grid.dart';
import 'package:yazlab2_2/components/keyboard_row.dart';
import 'package:yazlab2_2/providers/controller.dart';
import 'package:yazlab2_2/providers/theme_provider.dart';
import 'package:yazlab2_2/services/word_repository.dart';

class HomePage extends StatefulWidget {
  

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  late Future<List<String>> _wordsFuture;

  @override
  void initState() {
    super.initState();
    final controller = Provider.of<Controller>(context, listen: false);
    _wordsFuture = WordRepository.loadWordList(controller.gridSize);

   
    
  }

  void loadGameData(String gameId) {
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Wordle - Game:'),  
        centerTitle: true,
        elevation: 0,
        actions: [
          IconButton(
            onPressed: () {
              Provider.of<ThemeProvider>(context, listen: false).setTheme();
            },
            icon: const Icon(Icons.settings)
          )
        ],
      ),
      body: FutureBuilder<List<String>>(
        future: _wordsFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.done && snapshot.hasData) {
            final words = snapshot.data!;
            final r = Random().nextInt(words.length);
            final word = words[r];
            WidgetsBinding.instance?.addPostFrameCallback((_) {
              Provider.of<Controller>(context, listen: false).setCorrectWord(word: word);
            });

            return _buildGameInterface();
          } else {
            return const Center(child: CircularProgressIndicator());
          }
        },
      ),
    );
  }

  Widget _buildGameInterface() {
    final controller = Provider.of<Controller>(context);
    return Column(
      children: [
        const Divider(height: 1, thickness: 2),
        Expanded(
          flex: 7,
          child: Padding(
            padding: const EdgeInsets.fromLTRB(0, 10, 0, 0),
            child: Grid(
              crossAxisCount: controller.gridSize,
              totalTiles: controller.gridSize * 6,
            ),
          )
        ),
        Expanded(
          flex: 4,
          child: Padding(
            padding: const EdgeInsets.fromLTRB(0, 30, 0, 0),
            child: Column(
              children: const [
                KeyboardRow(min: 1, max: 12),
                KeyboardRow(min: 13, max: 23),
                KeyboardRow(min: 24, max: 34),
              ],
            ),
          )
        ),
      ],
    );
  }
}
