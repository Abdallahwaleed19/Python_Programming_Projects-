import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Container(child: Image.network("https://cdn1.rousingthekop.com/uploads/4/2024/08/GettyImages-2168469320-scaled.jpg"),),
        appBar: AppBar(
          backgroundColor: const Color.fromARGB(255, 35, 164, 182),
          title: Text(
            "footballer",
            style: TextStyle(
              fontSize: 30,
              fontWeight: FontWeight.bold,
              color: Color.fromARGB(255, 255, 255, 255),
            ),
          ),
        )
      ),
    );
  }
}
