import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       home: Scaffold(body: Center(child: Text("Welcome to Flutter"))),
//     );
//   }
// }

// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       home: Scaffold(
//         body: Column(
//           children: [
//             ElevatedButton(onPressed: () {}, child: Text("Click Me")),
//             SizedBox(height: 20), // Add some space between buttons
//             ElevatedButton(onPressed: () {}, child: Text("Click Me Too")),
//             SizedBox(height: 20), // Add some space between buttons
//             ElevatedButton(onPressed: () {}, child: Text("Click Me Three")),

//           ],
//         ),
//       ),
//     );
//   }
// }

// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       home: Scaffold(
//         body: Container(
//           child: Text("طيزك حمرا"),
//           color : Colors.blue ,
//           margin: EdgeInsets.all(10),
//         ),
//       ),
//     );
//   }
// }

// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       home: Scaffold(
//         body: Center (
//           child:  Container(
//           width: 100,
//           height: 100,
//           child: Center(child: Text("Hello")),
//           decoration: BoxDecoration(
//             color: Colors.blue,
//             borderRadius: BorderRadius.circular(10),
//             border: Border.all(color: Colors.red, width: 2),
//           ),
//          ) ),
//       ),
//     );
//   }
// }

// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       home: Scaffold(
//         body: Row(
//           mainAxisAlignment: MainAxisAlignment.spaceEvenly,
//           children: [
//             Icon(Icons.house),
//           ],
//         ),
//       ),
//     );
//   }
// }

// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       home: Scaffold(
//         body: CircleAvatar(
//           radius: 50,
//           child: Icon(Icons.person),
//           backgroundColor: Colors.green,
//         ),
//       ),
//     );
//   }
// }

// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       home: Scaffold(
//       body: SafeArea(
//         child: Center(child: Text("Hello Flutter") )
//     ) ,
//       ),
//     );
//   }
// }

// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context){
//     return MaterialApp(
//       home: Scaffold(
//         body: SingleChildScrollView(
//           child:ListView.builder(
//                 itemCount: 20,
//                 itemBuilder: (context, index) {
//                 return ListTile(
//                      title: Text('Item ${index + 1}'),
//                               );
//                          },
//          )
//         ),
//       ),
//     );
//   }
// }

// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       home: Scaffold(
//         body: TextField(
//           decoration: InputDecoration(
//             border: OutlineInputBorder(),
//             labelText: 'Enter your name',
//           ),
//         ),
//       ),
//     );
//   }
// }

// class MyApp extends StatelessWidget{
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       home: Scaffold(
//         appBar: AppBar(
//           title: Text("My Page"),
//         ),
//         body: Column(
//           children: [
//             CircleAvatar(
//               radius: 40,
//               backgroundImage: AssetImage('assets/profile.png'),
//             ),
//             Row(
//               mainAxisAlignment: MainAxisAlignment.spaceEvenly,
//               children: [
//                 Icon(Icons.home),
//                 Icon(Icons.search),
//                 Icon(Icons.settings),
//               ],
//             )
//           ],
//         ),
//       ),
//     );
//   }
// }

// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       home: Scaffold(
//         body: Builder(
//           builder: (context) {
//             return ElevatedButton(
//               onPressed: () {
//                 showDialog(
//                   context: context,
//                   builder: (context) {
//                     return AlertDialog(
//                       title: Text('Warning!'),
//                       content: Text("Are you Sure ?"),
//                       actions: [
//                         TextButton(onPressed: () => Navigator.pop(context), child: Text("Yes")),
//                         TextButton(onPressed: () => Navigator.pop(context), child: Text("No")),
//                       ]
//                     );
//                   }
//                 );
//               },
//               child: Text("Show dialog"),
//             );
//           }
//         )
//       )
//     );
//   }
// }

// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       initialRoute: '/',
//       routes: {
//         '/': (context) => HomePage(),
//         '/details': (context) => DetailsPage(),
//       },
//     );
//   }
// }


