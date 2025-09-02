import 'package:flutter/material.dart';
import 'package:login_page/Features/auth/registration/controllers/registration_controller.dart';
import 'package:login_page/core/validator.dart';
import '../components/my_registration_widget.dart';

class RegistrationPage extends StatefulWidget {
  const RegistrationPage({super.key});

  @override
  State<RegistrationPage> createState() => _RegistrationPageState();
}

class _RegistrationPageState extends State<RegistrationPage> {
  final _firstNameController = TextEditingController();
  final _lastNameController = TextEditingController();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  final _confirmPasswordController = TextEditingController();

  String? _firstNameError;
  String? _lastNameError;
  String? _emailError;
  String? _passwordError;
  String? _confirmPasswordError;

  final RegistrationController _controller = RegistrationController();
  final _formKey = GlobalKey<FormState>();

  @override
  void dispose() {
    _firstNameController.dispose();
    _lastNameController.dispose();
    _emailController.dispose();
    _passwordController.dispose();
    _confirmPasswordController.dispose();
    super.dispose();
  }

  Future<void> _validateAndSubmit() async {
    // Validate all fields
    setState(() {
      _firstNameError = Validator.validateName(_firstNameController.text, 'First name');
      _lastNameError = Validator.validateName(_lastNameController.text, 'Last name');
      _emailError = Validator.validateEmail(_emailController.text);
      _passwordError = Validator.validatePassword(_passwordController.text);
      _confirmPasswordError = Validator.validateConfirmPassword(
        _confirmPasswordController.text,
        _passwordController.text,
      );
    });

    // Check if any errors exist
    if (_firstNameError != null ||
        _lastNameError != null ||
        _emailError != null ||
        _passwordError != null ||
        _confirmPasswordError != null) {
      return;
    }

    try {
      final user = _controller.registerUser(
        firstName: _firstNameController.text,
        lastName: _lastNameController.text,
        email: _emailController.text,
        password: _passwordController.text,
        confirmPassword: _confirmPasswordController.text,
      );

      if (user != null && mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('Registration Successful')),
        );
        // Optionally navigate to another page
        // Navigator.of(context).pushReplacement(...);
      }
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Registration failed: ${e.toString()}')),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Sign Up')),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Form(
            key: _formKey,
            child: Column(
              children: [
                RegistrationFormField(
                  controller: _firstNameController,
                  labelText: 'First Name',
                  errorText: _firstNameError,
                  onChanged: (value) {
                    setState(() {
                      _firstNameError = Validator.validateName(value, 'First name');
                    });
                  },
                ),
                const SizedBox(height: 16),
                RegistrationFormField(
                  controller: _lastNameController,
                  labelText: 'Last Name',
                  errorText: _lastNameError,
                  onChanged: (value) {
                    setState(() {
                      _lastNameError = Validator.validateName(value, 'Last name');
                    });
                  },
                ),
                const SizedBox(height: 16),
                RegistrationFormField(
                  controller: _emailController,
                  labelText: 'Email',
                  keyboardType: TextInputType.emailAddress,
                  errorText: _emailError,
                  onChanged: (value) {
                    setState(() {
                      _emailError = Validator.validateEmail(value);
                    });
                  },
                ),
                const SizedBox(height: 16),
                RegistrationFormField(
                  controller: _passwordController,
                  labelText: 'Password',
                  obscureText: true,
                  errorText: _passwordError,
                  onChanged: (value) {
                    setState(() {
                      _passwordError = Validator.validatePassword(value);
                    });
                  },
                ),
                const SizedBox(height: 16),
                RegistrationFormField(
                  controller: _confirmPasswordController,
                  labelText: 'Confirm Password',
                  obscureText: true,
                  errorText: _confirmPasswordError,
                  onChanged: (value) {
                    setState(() {
                      _confirmPasswordError = Validator.validateConfirmPassword(
                        value,
                        _passwordController.text,
                      );
                    });
                  },
                ),
                const SizedBox(height: 24),
                ElevatedButton(
                  onPressed: _validateAndSubmit,
                  style: ElevatedButton.styleFrom(
                    minimumSize: const Size(double.infinity, 50),
                  ),
                  child: const Text('Register'),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}