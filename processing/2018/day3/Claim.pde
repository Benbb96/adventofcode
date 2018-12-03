class Claim {
  
  int id;
  PVector position, size;
  color colour;
  boolean hide = false;
  
  Claim(int id, PVector position, PVector size) {
    this.id = id;
    this.position = position;
    this.size = size;
    this.colour = color(random(255), random(255), random(255));
  }
  
  void display() {
    if (!this.hide) {
      fill(this.colour);
      noStroke();
      rect(this.position.x, this.position.y, this.size.x, this.size.y);
      //fill(255,255,255);
      //text(str(this.id), this.position.x + this.size.x, this.position.y + this.size.y);
    }
  }
  
  boolean doOverlap(Claim claim) {
    PVector l1 = new PVector(this.position.x, this.position.y);
    PVector r1 = new PVector(this.position.x + this.size.x, this.position.y + this.size.y);
    PVector l2 = new PVector(claim.position.x, claim.position.y);
    PVector r2 = new PVector(claim.position.x + claim.size.x, claim.position.y + claim.size.y);
    
    // If one rectangle is on left side of other 
    if (l1.x > r2.x || l2.x > r1.x) 
        return false; 
  
    // If one rectangle is above other 
    if (l1.y < r2.y || l2.y < r1.y) 
        return false; 
    return true; 
  }
  
  void hide() {
    this.hide = true;
  }
  
  String infos() {
    return "Id " + str(this.id) +
    "\t|| Position : " + str(position.x) + ", " + str(position.y) +
    "\t|| Size : " + str(size.x) + ", " + str(size.y);
  }
  
}
