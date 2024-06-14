#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

// Example image data generated from the Python script
const unsigned char PROGMEM image[SCREEN_HEIGHT][SCREEN_WIDTH] = 
"Clipboard Content"
;

void setup() {
    // Initialize the display
    if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { // Address 0x3C for 128x64
        Serial.println(F("SSD1306 allocation failed"));
        for(;;); // Don't proceed, loop forever
    }

    // Clear the buffer
    display.clearDisplay();

    // Loop through the image array and set pixels on the display
    for (int y = 0; y < SCREEN_HEIGHT; y++) {
        for (int x = 0; x < SCREEN_WIDTH; x++) {
            if (pgm_read_byte(&image[y][x]) != 0) {
                display.drawPixel(x, y, SSD1306_WHITE);
            } else {
                display.drawPixel(x, y, SSD1306_BLACK);
            }
        }
    }

    // Display the image
    display.display();
}

void loop() {
    // Nothing to do here
}
