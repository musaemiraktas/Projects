import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';

class AuthService {
  final FirebaseAuth _auth = FirebaseAuth.instance;
  final FirebaseFirestore _firestore = FirebaseFirestore.instance;

  String getUsernameFromEmail(String email) {
    return email.split('@').first;
  }

 
  Future<User?> signUp(String email, String password) async {
    try {
      UserCredential userCredential = await _auth.createUserWithEmailAndPassword(email: email, password: password);

      // E-posta adresinden kullanıcı adını al
      String username = getUsernameFromEmail(email);

      // Kullanıcı bilgilerini Firestore'a kaydet
      await _firestore.collection('users').doc(userCredential.user!.uid).set({
        'username': username,
        'email': email
      });

      return userCredential.user; // Kullanıcıyı döndür
    } catch (e) {
      print(e.toString());
      return null;
    }
  }

 
  Future<User?> signIn(String email, String password) async {
    try {
      UserCredential userCredential = await _auth.signInWithEmailAndPassword(email: email, password: password);
      return userCredential.user;
    } catch (e) {
      print(e.toString());
      return null;
    }
  }
}
