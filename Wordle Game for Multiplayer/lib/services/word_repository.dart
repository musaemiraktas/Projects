import 'package:flutter/services.dart' show rootBundle;

class WordRepository {
  // Belirli bir boyuttaki kelime listesini yükler
  static Future<List<String>> loadWordList(int gridSize) async {
    final String content = await rootBundle.loadString('assets/${gridSize}words.txt');
    return content.split('\n').map((word) => word.trim()).where((word) => word.isNotEmpty).toList();
  }

  // Girilen kelimenin geçerli olup olmadığını kontrol eder
  static Future<bool> isValidWord(String inputWord, int gridSize) async {
    List<String> words = await loadWordList(gridSize);
    return words.contains(inputWord.toUpperCase());
  }
}
