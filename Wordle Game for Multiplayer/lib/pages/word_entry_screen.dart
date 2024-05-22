import 'package:flutter/material.dart';

class WordEntryScreen extends StatefulWidget {
  final int columnCount;


  WordEntryScreen({Key? key, required this.columnCount})
      : super(key: key);

  @override
  _WordEntryScreenState createState() => _WordEntryScreenState();
}

class _WordEntryScreenState extends State<WordEntryScreen> {
  String enteredWord = '';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Kelime Girişi'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              'Kelimenizi Girin',
              style: TextStyle(fontSize: 20),
            ),
            SizedBox(height: 20),
            _buildWordInputField(),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                
                print('Girilen Kelime: $enteredWord');
              },
              child: Text('Gönder'),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildWordInputField() {
    return Container(
      width: 200,
      child: TextField(
        onChanged: (value) {
          setState(() {
            enteredWord = value;
          });
        },
        maxLength: widget.columnCount, 
        decoration: InputDecoration(
          labelText: 'Kelime',
          border: OutlineInputBorder(),
        ),
      ),
    );
  }
}
