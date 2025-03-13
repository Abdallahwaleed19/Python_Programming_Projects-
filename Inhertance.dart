// class Person {
//   String? name;
//   int? age;

//   void display() {
//     print("The person name is : $name , and his age is : $age ");
//   }
// }

// class Employee extends Person {
//   int? employeeId;
//   String? companyName;
//   String? departmentName;

//   void displayInfo() {
//     print("The Employee Name : $name , and his Age : $age");
//     print(
//       "The Employee Id : $employeeId , and his Company Name : $companyName , and his Department is : $departmentName ",
//     );
//   }
// }

// void main() {
//   var employee = Employee();
//   employee.name = "Abdallah";
//   employee.age = 20;
//   employee.employeeId = 20230192;
//   employee.companyName = "Menoufia National University";
//   employee.departmentName = "IoT Teaching Assistant";
//   employee.display();
//   employee.displayInfo();
// }

// Inhertance of Constructor

// class Laptop {
//   Laptop() {
//     print("laptop constructor");
//   }
// }

// class Dell extends Laptop {
//   Dell(){
//     print("Dell constructor");
//   }
// }

// void main() {
//   var dell = Dell();
// }

// class Laptop {
//   Laptop(String name, String color) {
//     print("Laptop constructor");
//     print("Name : $name");
//     print("Color: $color");
//   }
// }

// class Dell extends Laptop {
//   Dell(String name, String color) : super(name, color) {
//     print("Dell constructor");
//   }
// }

// void main() {
//   var dell = Dell("Dell Inspiron", "Black");
// }

// class laptop {
//   void show() {
//     print("Laptop show method");
//   }
// }

// class Dell extends laptop {
//   void show() {
//     super.show();
//     print("Dell show method");
//   }
// }
// void main(){
//   Dell dell = Dell();
//   dell.show();
// }

// Overriding
// class Car {
//   String? brand;
//   int? speed;

//   Car({this.brand, this.speed});

//   void power() {
//     print("The power is petrol");
//   }
// }

// class Tesla extends Car {
//   Tesla(String brand, int speed) : super(brand: brand, speed: speed);

//   @override
//   void power() {
//     print("The power is Electricity"); // override the power method
//   }
// }

// void main() {
//   Car car = Car(brand: "Toyota", speed: 120);
//   car.power();
//   print('Brand: ' + car.brand.toString() + ', Speed: ' + car.speed.toString());
//   Tesla tesla = Tesla("V1", 220);
//   print('Brand: ' + tesla.brand.toString() + ', Speed: ' + tesla.speed.toString());
//   tesla.power();
// }


