import '../../../../core/validator.dart';
import '../models/user_model.dart';

class RegistrationController {

  User? registerUser({
    required String firstName,
    required String lastName,
    required String email,
    required String password,
    String? confirmPassword,
  }) {
    final firstNameError = Validator.validateName(firstName, 'First name');
    final lastNameError = Validator.validateName(lastName, 'Last name');
    final emailError = Validator.validateEmail(email);
    final passwordError = Validator.validatePassword(password);
    final confirmPasswordError = confirmPassword != null 
        ? Validator.validateConfirmPassword(confirmPassword, password)
        : null;

    if (firstNameError != null || 
        lastNameError != null || 
        emailError != null || 
        passwordError != null || 
        confirmPasswordError != null) {
      return null;
    }

    return User(
      firstName: firstName,
      lastName: lastName,
      email: email,
      password: password,
    );
  }
}