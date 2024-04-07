#include <Adafruit_GPS.h>
void setup() {
  GPS.sendCommand(PMTK_SET_NEMA_OUTPUT_RMCGGA);
}

void loop() {
  
}
