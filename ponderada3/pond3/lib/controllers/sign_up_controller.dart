import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:pond3/services/notification.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';

class SignUpController {
  Future<void> register(
      BuildContext context,
      TextEditingController usernameController,
      TextEditingController emailController,
      TextEditingController passwordController,
      Function setState,
      Function setLoading,
      Function setErrorMessage) async {
    setLoading(true);
    setErrorMessage('');

    try {
      final String? url = dotenv.env['URL'];
      final String? userManagement = dotenv.env['USER_MANAGEMENT'];

      final response = await http.post(
        Uri.parse('$url/$userManagement/users'),
        body: jsonEncode({
          'username': usernameController.text,
          'email': emailController.text,
          'password': passwordController.text,
        }),
        headers: {'Content-Type': 'application/json'},
      );

      setLoading(false);

      if (response.statusCode >= 200 && response.statusCode < 300) {
        final data = jsonDecode(response.body);
        final String? username = data['username'];
        final String? email = data['email'];
        final String action = 'register';
        final String datetime = DateTime.now().toIso8601String();
        final String? logger = dotenv.env['LOGGER'];

        await http.post(
          Uri.parse('$url/$logger/log'),
          body: jsonEncode({
            'username': username,
            'email': email,
            'action': action,
            'datetime': datetime,
          }),
          headers: {'Content-Type': 'application/json'},
        );

        NotificationService.showNotification('Registration successful',
            'You have successfully registered. Please login to continue.');

        Navigator.pop(context);
      } else {
        setErrorMessage('Failed to register');
      }
    } catch (e) {
      setLoading(false);
      setErrorMessage('Failed to register');
    }
  }
}
