class Validator {
  static String? validateName(String value, String fieldName) {
    if (value.isEmpty) return "Please enter your $fieldName";
    if (!RegExp(r'^[a-zA-Z]').hasMatch(value)) {
      return '$fieldName must start with a letter';
    }
    if (value.length > 8) {
      return '$fieldName must be at most 8 characters';
    }
    return null;
  }

  static String? validateEmail(String value) {
    if (value.isEmpty) return 'Please enter your email';
    if (!value.contains('@')) return 'Please enter a valid email';
    return null;
  }

  static String? validatePassword(String value) {
    if (value.isEmpty) return 'Please enter a password';
    if (value.length < 6) return 'Password must be at least 6 characters';
    return null;
  }

  static String? validateConfirmPassword(String confirm, String password) {
    if (confirm != password) return 'Passwords do not match';
    return null;
  }
}