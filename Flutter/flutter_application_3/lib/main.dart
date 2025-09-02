// Main entry point
import 'package:flutter/material.dart';

void main() {
  runApp(LanguageLearningApp());
}

class LanguageLearningApp extends StatelessWidget {
  const LanguageLearningApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AI Language Learning',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: LoginPage(),
    );
  }
}

// Login Page
class LoginPage extends StatelessWidget {
  const LoginPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: ElevatedButton(
          child: Text('Login'),
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (_) => ChooseLanguagePage()),
            );
          },
        ),
      ),
    );
  }
}

// Choose Language Page
class ChooseLanguagePage extends StatelessWidget {
  final List<String> languages = ['English', 'Arabic', 'Spanish'];

   ChooseLanguagePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Choose Language')),
      body: ListView(
        children: languages.map((lang) => ListTile(
          title: Text(lang),
          onTap: () => Navigator.push(
            context,
            MaterialPageRoute(builder: (_) => LessonsOverviewPage(language: lang)),
          ),
        )).toList(),
      ),
    );
  }
}

// Lessons Overview Page
class LessonsOverviewPage extends StatelessWidget {
  final String language;
  const LessonsOverviewPage({super.key, required this.language});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('$language Lessons')),
      body: ListView.builder(
        itemCount: 5,
        itemBuilder: (_, index) => ListTile(
          title: Text('Lesson ${index + 1}'),
          onTap: () => Navigator.push(
            context,
            MaterialPageRoute(builder: (_) => LessonDetailsPage(lessonNumber: index + 1)),
          ),
        ),
      ),
    );
  }
}

// Lesson Details Page
class LessonDetailsPage extends StatelessWidget {
  final int lessonNumber;
  const LessonDetailsPage({super.key, required this.lessonNumber});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Lesson $lessonNumber Details')),
      body: Column(
        children: [
          Text('Lesson $lessonNumber content goes here.'),
          ElevatedButton(
            child: Text('Start Quiz'),
            onPressed: () => Navigator.push(
              context,
              MaterialPageRoute(builder: (_) => QuizPage()),
            ),
          )
        ],
      ),
    );
  }
}

// Quiz Page
class QuizPage extends StatelessWidget {
  const QuizPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Quiz')),
      body: Center(child: Text('Quiz Content Here')),
    );
  }
}

// Vocabulary Flashcards Page
class VocabularyFlashcardsPage extends StatelessWidget {
  final List<String> vocab = ['Apple - تفاحة', 'Book - كتاب', 'Car - سيارة'];

   VocabularyFlashcardsPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Flashcards')),
      body: ListView(
        children: vocab.map((word) => Card(
          child: Padding(
            padding: const EdgeInsets.all(16.0),
            child: Text(word, style: TextStyle(fontSize: 20)),
          ),
        )).toList(),
      ),
    );
  }
}

// Progress Tracker Page
class ProgressTrackerPage extends StatelessWidget {
  const ProgressTrackerPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Progress Tracker')),
      body: Center(child: Text('Your progress will be shown here.')),
    );
  }
}

// Practice Speaking Page
class PracticeSpeakingPage extends StatelessWidget {
  const PracticeSpeakingPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Practice Speaking')),
      body: Center(child: Text('Microphone input simulation goes here.')),
    );
  }
}

// AI Tutor Chatbot Page
class ChatbotPage extends StatelessWidget {
  const ChatbotPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('AI Tutor')),
      body: Center(child: Text('Chat with AI Tutor here.')),
    );
  }
}

// Settings Page
class SettingsPage extends StatelessWidget {
  const SettingsPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Settings')),
      body: ListView(
        children: [
          ListTile(title: Text('Language')), 
          ListTile(title: Text('Theme')),
        ],
      ),
    );
  }
}
