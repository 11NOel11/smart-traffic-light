// Arduino Traffic Light Controller for 4-way Intersection
// Each direction has 3 LEDs: Red, Yellow, Green

const int redPins[4]    = {2, 5, 8, 11};
const int yellowPins[4] = {3, 6, 9, 12};
const int greenPins[4]  = {4, 7, 10, 13};

int currentGreen = 0; // Start with direction 0 green

void setSignal(int greenIndex);
void turnAllRed();
void transitionYellow(int fromDir);

void setup() {
  Serial.begin(9600);

  for (int i = 0; i < 4; i++) {
    pinMode(redPins[i], OUTPUT);
    pinMode(yellowPins[i], OUTPUT);
    pinMode(greenPins[i], OUTPUT);
  }

  setSignal(currentGreen); // Start with green to direction 0
}

void loop() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');
    int greenDir = input.toInt();

    if (greenDir >= 0 && greenDir < 4 && greenDir != currentGreen) {
      transitionYellow(currentGreen); // Add yellow transition
      turnAllRed();
      delay(1000); // All-red buffer
      setSignal(greenDir);
      currentGreen = greenDir;
    } else if (greenDir == currentGreen) {
      Serial.println("Direction already green.");
    } else {
      Serial.println("Invalid input. Enter number 0 to 3.");
    }
  }
}

// Set green for one direction, red for all others
void setSignal(int greenIndex) {
  for (int i = 0; i < 4; i++) {
    digitalWrite(redPins[i], i == greenIndex ? LOW : HIGH);
    digitalWrite(yellowPins[i], LOW);
    digitalWrite(greenPins[i], i == greenIndex ? HIGH : LOW);
  }

  Serial.print("Green light assigned to direction ");
  Serial.println(greenIndex);
}

// Brief yellow transition from green
void transitionYellow(int fromDir) {
  digitalWrite(greenPins[fromDir], LOW);
  digitalWrite(yellowPins[fromDir], HIGH);
  delay(2000); // Yellow for 2 seconds
  digitalWrite(yellowPins[fromDir], LOW);
}

// Turn all red (no green or yellow active)
void turnAllRed() {
  for (int i = 0; i < 4; i++) {
    digitalWrite(greenPins[i], LOW);
    digitalWrite(yellowPins[i], LOW);
    digitalWrite(redPins[i], HIGH);
  }
}
