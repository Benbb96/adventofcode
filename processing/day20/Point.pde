class Point {
  
  int id;
  PVector position, velocity, acceleration;
  
  Point(int id, PVector position, PVector velocity, PVector acceleration) {
    this.id = id;
    this.position = position;
    this.velocity = velocity;
    this.acceleration = acceleration;
  }
  
  void display() {
    pushMatrix();
    // Draw the sphere at its position
    translate(position.x, position.y, position.z);
    sphere(sphereSize);
    popMatrix();
  }
  
  String infos() {
    return "Id " + str(this.id) +
    "\t|| Position : " + str(position.x) + ", " + str(position.y) + ", " + str(position.z) +
    "\t|| Velocity : " + str(velocity.x) + ", " + str(velocity.y) + ", " + str(velocity.z) +
    "\t|| Acceleration : " + str(acceleration.x) + ", " + str(acceleration.y) + ", " + str(acceleration.z);
  }
  
  void update() {
    velocity.x += acceleration.x;
    velocity.y += acceleration.y;
    velocity.z += acceleration.z;
    position.x += velocity.x;
    position.y += velocity.y;
    position.z += velocity.z;
  }
  
  int distance() {
    return int(abs(position.x) + abs(position.y) + abs(position.z));
  }
  
}