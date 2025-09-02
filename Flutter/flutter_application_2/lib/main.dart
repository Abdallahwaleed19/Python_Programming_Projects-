import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Static Text",
      theme: ThemeData(primarySwatch: Colors.blue),
      home: HomeScreen(),
    );
  }
}

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Static Text"),
        actions: [
          IconButton(
            onPressed: () {}, // define onPressed function
            icon: Icon(Icons.menu), // define icon
          ),
        ],
      ),
      body: Center(
        child: Text("Static Text"),
      ),
    );
  }
}
