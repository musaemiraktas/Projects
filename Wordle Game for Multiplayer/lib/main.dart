import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:yazlab2_2/pages/home_page.dart';
import 'package:yazlab2_2/pages/sign_in_page.dart';
import 'package:yazlab2_2/pages/grid_size_selection_page.dart';
import 'package:yazlab2_2/providers/controller.dart';
import 'package:yazlab2_2/providers/theme_provider.dart';
import 'package:yazlab2_2/services/auth_service.dart';
import 'package:yazlab2_2/themes/themes.dart';
import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );

  runApp(MultiProvider(
    providers: [
      ChangeNotifierProvider(create: (_) => Controller()),
      ChangeNotifierProvider(create: (_) => ThemeProvider()),
      Provider<AuthService>(create: (_) => AuthService()),
    ],
    child: MyApp(),
  ));
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Consumer<ThemeProvider>(
      builder: (_, themeProvider, __) => MaterialApp(
        title: 'Wordle Clone',
        theme: themeProvider.isDark ? darkTheme : lightTheme,
        debugShowCheckedModeBanner: false,
        initialRoute: '/',
        routes: {
          '/': (context) => HomePage(),  //HomePage()
          '/gridSizeSelection': (context) => GridSizeSelectionPage(),
          '/game': (context) => HomePage(),
        },
      ),
    );
  }
}
