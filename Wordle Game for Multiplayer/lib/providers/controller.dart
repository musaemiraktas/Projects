import 'package:flutter/material.dart';
import 'package:yazlab2_2/constants/answer_stages.dart';
import 'package:yazlab2_2/data/keys_map.dart';
import 'package:yazlab2_2/models/tile_model.dart';
import 'package:yazlab2_2/services/word_repository.dart';

class Controller extends ChangeNotifier{

  int gridSize = 5; // Varsayılan değer

  void setGridSize(int size) {
    gridSize = size;
    notifyListeners();
  }

  List<String> words = [];

  Controller() {
    _loadWords();
  }

  Future<void> _loadWords() async {
    words = await WordRepository.loadWordList(gridSize);
  }

  bool isValidWord(String inputWord) {
    return words.contains(inputWord.toUpperCase());
  }

  String correctWord = "";


  int currentTile = 0, currentRow = 0;

  List <TileModel> tilesEntered = [];

  setCorrectWord({required String word}) => correctWord = word;
  setKeyTapped({required String value}){
    if(value == 'ENTER'){
      if(currentTile == gridSize * (currentRow + 1)){
        checkWord();
        print(correctWord);
      }
    }
    else if(value == 'SİL'){
      if(currentTile > gridSize * (currentRow + 1) - gridSize){
        currentTile--;
        tilesEntered.removeLast();
      }
    }
    else{
      if(currentTile < gridSize * (currentRow + 1)){
        tilesEntered.add(TileModel(letter: value, answerStage: AnswerStage.notAnswered));
        currentTile++;
      }
    }

    notifyListeners();
  }

  checkWord() async {
    List<String> guessed = [], remainingCorrect = [];
    String guessedWord = "";


    for(int i = currentRow * gridSize; i< (currentRow * gridSize) + gridSize; i++){
      guessed.add(tilesEntered[i].letter);
    }

    guessedWord = guessed.join();

    bool isValid = await WordRepository.isValidWord(guessedWord, gridSize);
  if (!isValid) {
    
    print("Geçersiz kelime, başka bir kelime deneyin.");
    return;
  }





    remainingCorrect = correctWord.characters.toList();

    if(guessedWord == correctWord){
      for(int i = currentRow * gridSize; i< (currentRow * gridSize) + gridSize; i++){
      tilesEntered[i].answerStage = AnswerStage.correct;
      keysMap.update(tilesEntered[i].letter, (value) => AnswerStage.correct);
    }
    }
    else{
      for(int i=0; i<gridSize; i++){
        if(guessedWord[i] == correctWord[i]){
          remainingCorrect.remove(guessedWord[i]);
          tilesEntered[i + (currentRow * gridSize)].answerStage = AnswerStage.correct;
          keysMap.update(guessedWord[i], (value) => AnswerStage.correct);
        }
      }

      for(int i = 0; i < remainingCorrect.length; i++){
        for(int j=0; j<gridSize; j++){
          if(remainingCorrect[i] == tilesEntered[j + (currentRow * gridSize)].letter){

            if(tilesEntered[j + (currentRow * gridSize)].answerStage != AnswerStage.correct){
              tilesEntered[j + (currentRow * gridSize)].answerStage = AnswerStage.contains;
            }

            final resultKey = keysMap.entries.where((element) => element.key == tilesEntered[j + (currentRow * gridSize)].letter);
            
            if(resultKey.single.value != AnswerStage.correct){
              keysMap.update(resultKey.single.key, (value) => AnswerStage.contains);
            }
          }
        }
      }
    }


    for(int i = currentRow * gridSize; i< (currentRow * gridSize) + gridSize; i++){
      if(tilesEntered[i].answerStage == AnswerStage.notAnswered){
        tilesEntered[i].answerStage = AnswerStage.incorrect;
        keysMap.update(tilesEntered[i].letter, (value) => AnswerStage.incorrect);
      }
    }

    currentRow++;
    notifyListeners();
  }

}