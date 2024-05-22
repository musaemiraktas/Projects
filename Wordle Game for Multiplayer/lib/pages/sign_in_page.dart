import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:yazlab2_2/pages/grid_size_selection_page.dart';
import 'package:yazlab2_2/pages/home_page.dart';

import '../services/auth_service.dart';

class SignInPage extends StatefulWidget {
  @override
  _SignInPageState createState() => _SignInPageState();
}

class _SignInPageState extends State<SignInPage> {
  final AuthService _auth = AuthService();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Kayıt ve Giriş"),
        centerTitle: true,
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: <Widget>[
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20.0),
            child: TextField(
              controller: _emailController,
              decoration: InputDecoration(labelText: 'Kullanıcı Adı (Email)'),
            ),
          ),
          Padding(
            padding:
                const EdgeInsets.symmetric(horizontal: 20.0, vertical: 8.0),
            child: TextField(
              controller: _passwordController,
              obscureText: true,
              decoration: InputDecoration(labelText: 'Şifre'),
            ),
          ),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20.0),
            child: ElevatedButton(
              onPressed: () async {
                try {
                  var user = await _auth.signUp(
                      _emailController.text, _passwordController.text);
                  if (user != null) {
                    ScaffoldMessenger.of(context).showSnackBar(
                      SnackBar(
                        content: Text('Kayıt başarılı! Hoşgeldiniz!'),
                        backgroundColor: Colors.green,
                      ),
                    );
                    
                    Navigator.pushReplacement(
                      context,
                      MaterialPageRoute(builder: (context) => GridSizeSelectionPage()),
                    );
                  } else {
                    ScaffoldMessenger.of(context).showSnackBar(
                      SnackBar(
                        content: Text('Kayıt başarısız. Lütfen tekrar deneyin.'),
                        backgroundColor: Colors.red,
                      ),
                    );
                  }
                } catch (e) {
                  String errorMessage = 'Bir hata oluştu';
                  if (e is FirebaseException) {
                    errorMessage = e.message ?? 'Bilinmeyen bir hata oluştu.';
                  }
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(
                      content: Text('Kayıt başarısız: $errorMessage'),
                      backgroundColor: Colors.red,
                    ),
                  );
                }
              },
              child: Text('Kayıt Ol'),
              style: ElevatedButton.styleFrom(
                foregroundColor: Colors.white,
                backgroundColor: Colors.blue,
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20.0),
            child: ElevatedButton(
              child: Text('Giriş Yap'),
              onPressed: () async {
                var user = await _auth.signIn(
                    _emailController.text, _passwordController.text);
                if (user != null) {
                  
                  Navigator.pushReplacement(
                    context,
                    MaterialPageRoute(builder: (context) => GridSizeSelectionPage()),
                  );
                } else {
                  showDialog(
                    context: context,
                    builder: (context) {
                      return AlertDialog(
                        title: Text('Giriş Başarısız'),
                        content: Text(
                            'Lütfen bilgilerinizi kontrol edin ve tekrar deneyin.'),
                        actions: <Widget>[
                          TextButton(
                            child: Text('Tamam'),
                            onPressed: () {
                              Navigator.of(context).pop();
                            },
                          ),
                        ],
                      );
                    },
                  );
                }
              },
            ),
          ),
        ],
      ),
    );
  }
}
