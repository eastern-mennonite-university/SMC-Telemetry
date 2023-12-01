/*
 * Adafruit MCP2515 CAN Example Code from https://learn.adafruit.com/adafruit-rp2040-can-bus-feather/can-bus-test-2
 */
#include <Adafruit_MCP2515.h>

#if defined(ARDUINO_ADAFRUIT_FEATHER_RP2040_CAN)
  #define CS_PIN PIN_CAN_CS
#endif

#define CAN_BAUDRATE (250000)

Adafruit_MCP2515 mcp(CS_PIN);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  while(!Serial) delay(10);

  Serial.println("Init");

  if (!mcp.begin(CAN_BAUDRATE)) {
    Serial.println("Error initializing MCP2515");
    while(1) delay(10);
  }
  Serial.println("MCP2515 chip found");
}

void loop() {
  // put your main code here, to run repeatedly:
  int packetSize = mcp.parsePacket();

  if (packetSize) {
    Serial.print("Received ");

    if (mcp.packetExtended()) {
      Serial.print("extended ");
    }

    if (mcp.packetRtr()) {
      Serial.print("RTR ");
    }

    Serial.print("packet with id 0x");
    Serial.print(mcp.packetId(), HEX);

    if (mcp.packetRtr()){
      Serial.print(" and requested length ");
      Serial.println(mcp.packetDlc());
    } else {
      Serial.print(" and length ");
      Serial.println(packetSize);

      // only print packet data for non-RTR packets
      while (mcp.available()) {
        Serial.print((char)mcp.read());
      }
      Serial.println();
    }

    Serial.println();
  }
}
