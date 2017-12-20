ArrayList<Point> list = new ArrayList<Point>();  // My list of point
ArrayList<Point> toDelete = new ArrayList<Point>();  // The list of point to delete

int listSize;
float sphereSize = 10;
float a = 0, b = 0;  // Variable to make it rotate along the x and y axis

boolean save = true;  // Save the frames if true
boolean collision = false;  // If point collide, they're deleted
boolean informations = false;  // Display the information on screen if true

float scale = 0.1;

Point closest;  // The closest point from the origin
int distance = 0;  // Store the distance between the closest point and the origin

void setup() {
  size(1120,640,P3D);
  parseFile();
  closest = list.get(0);  // Initialize closest point as the first one of the list
}

void draw() {
  background(0);
  
  // Display informations
  if (informations) {
    textSize(23);
    text("Frame " + str(frameCount), 20, 40, 0);
    text(str(listSize) + " stars", 20, 80, 0);
    text("Closest is " + str(closest.id) + " (" + str(distance) + ")", width - 350, height -20, 0);
  }
  
  prepareCamera();
  
  stroke(255);
  int min = 10000000;
  for (int i = 0 ; i < listSize; i++) {
    Point point = list.get(i);
    point.update();  // Do the calculation to move the point
    
    distance = point.distance();
    if (distance < min) {  // Check if this point is the closest
      min = distance;
      closest = point;
    }
    point.display();  // Draw the sphere
  }
  
  if (collision)
    checkCollision();
  
  showClosest();
  
  sphereSize *= 1.02;  // Increment the size of the point to let them see from far
  
  if (save) {
    saveFrame("final/frame-###.gif");
  }
}

void parseFile() {
  // Retrieve each point from the input text
  String[] lines;
  lines = loadStrings("input.txt");
  listSize = lines.length;
  for (int i = 0 ; i < listSize; i++) {
    String[] data = split(lines[i], '<');
    String pos = split(data[1], '>')[0];
    String vel = split(data[2], '>')[0];
    String acc = split(data[3], '>')[0];
    String[] p = split(pos, ',');
    String[] v = split(vel, ',');
    String[] a = split(acc, ',');
    PVector position = new PVector(int(p[0]), int(p[1]), int(p[2]));
    PVector velocity = new PVector(int(v[0]), int(v[1]), int(v[2]));
    PVector acceleration = new PVector(int(a[0]), int(a[1]), int(a[2]));
    Point point = new Point(i, position, velocity, acceleration);
    //println(point.infos());
    list.add(point);
  }
}

void drawAxis() {
  // Add the three lines corresponding of the x (red), y (green) and z (blue) axis
  stroke(255, 0, 0);
  line(-200, 0, 0, 200, 0, 0);
  stroke(0, 255, 0);
  line(0, -200, 0, 0, 200, 0);
  stroke(0, 0, 255);
  line(0, 0, -200, 0, 0, 200);
}

void prepareCamera() {
  // Translate to the center of the view
  translate(width/2, height/2, 0);
  
  // Make a nice rotation
  rotateX(a % (2 * PI));
  a -= 0.002;
  rotateY(b % (2 * PI));
  b += 0.0015;
  rotateZ(7*PI/4);
  
  drawAxis();
  
  // Gently zoom out
  scale *= 0.985;
  scale(scale);
}

void showClosest() {
  // Paint in red and make the the closest point from origin bigger
  pushMatrix();
  pushStyle();
  fill(255, 0, 0);
  stroke(255, 0, 0);
  translate(closest.position.x, closest.position.y, closest.position.z);
  sphere(sphereSize + 50);
  popStyle();
  popMatrix();
}

void checkCollision() {
  // Go through the list and check if two point have the same position
  for (int i = 0 ; i < listSize; i++) {
    Point point = list.get(i);
    for (int j = i+1; j < listSize; j++) {
      Point compare = list.get(j);
      if (point.position.equals(compare.position)) {
        // If the point are not in the delete list, add them
        if (! toDelete.contains(point))
          toDelete.add(point);
        if (! toDelete.contains(compare))
          toDelete.add(compare);
      }
    }
  }
  
  // Delete all the point that are in the delete list and decrease the list size
  for (int i = 0 ; i < toDelete.size(); i++) {
    Point point = list.get(i);
    list.remove(point);
    toDelete.remove(point);
    listSize--;
  }
}