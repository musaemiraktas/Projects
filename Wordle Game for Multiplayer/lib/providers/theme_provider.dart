import 'package:flutter/material.dart';

class ThemeProvider extends ChangeNotifier{
  bool isDark = true;


  setTheme(){
    isDark = !isDark;
    notifyListeners();
  }
}