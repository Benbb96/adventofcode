
ArrayList<Claim> list = new ArrayList<Claim>();  // My list of Claim

int listSize;
int i = 0;
int j = 1;

boolean save = false;  // Save the frames if true
boolean informations = false;  // Display the information on screen if true

void setup() {
  size(1000, 1000);
  parseFile();
}

void draw() {
  println("i=" + str(i));
   println("j=" + str(j));
  background(0);
  
  // Display informations
  if (informations) {
    textSize(23);
    text("Frame " + str(frameCount), 20, 40);
    text(str(listSize) + " claims", 20, 80);
  }
  
  stroke(255);
  for (int i = 0 ; i < listSize; i++) {
    Claim Claim = list.get(i);
    Claim.display();  // Draw the claim rectangle
  }
  
  if (list.get(i).doOverlap(list.get(j))) {
    list.get(i).hide();
    list.get(j).hide();
  }
  
  if (j < listSize)
    j++;
  else if (i < listSize) {
    i++;
    j = i+1;
  }
  
  if (save) {
    saveFrame("frames/###.gif");
  }
}

void parseFile() {
  // Retrieve each Claim from the input text
  String[] lines;
  lines = loadStrings("input.txt");
  listSize = lines.length;
  for (int i = 0 ; i < listSize; i++) {
    String[] data = split(lines[i], ' ');
    int id = int(data[0].substring(1,data[0].length()));
    int x = int(split(data[2], ',')[0]);
    String Y = split(data[2], ',')[1];
    int y = int(Y.substring(0, Y.length()-1));
    int l = int(split(data[3], 'x')[0]);
    int h = int(split(data[3], 'x')[1]);
    PVector position = new PVector(x, y);
    PVector size = new PVector(l, h);
    Claim Claim = new Claim(id, position, size);
    // println(Claim.infos());
    list.add(Claim);
  }
}
