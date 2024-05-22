import 'package:flutter/material.dart';
import 'package:yazlab2_2/constants/colors.dart';

final ThemeData lightTheme = ThemeData(
        primaryColorLight: lightThemeLightShade,
        primaryColorDark: lightThemeDarkShade,
        appBarTheme: const AppBarTheme(
          backgroundColor: Colors.white,
          titleTextStyle: TextStyle(
            color: Colors.black,
            fontSize: 20,
            fontWeight: FontWeight.bold,
          )
        ),
        scaffoldBackgroundColor: Colors.white,
        brightness: Brightness.light,
        textTheme: const TextTheme().copyWith(
          bodyText2: const TextStyle(fontWeight: FontWeight.bold,
          color: Colors.black,
          )
        )
);

final ThemeData darkTheme = ThemeData(
        
        primaryColorLight: darkThemeLightShade,
        primaryColorDark: darkThemeDarkShade,
        appBarTheme: const AppBarTheme(
          backgroundColor: Colors.black,
          titleTextStyle: TextStyle(
            color: Colors.white,
            fontSize: 20,
            fontWeight: FontWeight.bold,
          )
        ),
        scaffoldBackgroundColor: Colors.black,
        brightness: Brightness.dark, 
        textTheme: const TextTheme().copyWith(
          bodyText2: const TextStyle(fontWeight: FontWeight.bold,
          color: Colors.white,
          )
        )
);