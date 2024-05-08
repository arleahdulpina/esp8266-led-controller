void setup() {
  // put your setup code here, to run once:
pinMode(led,OUTPUT);
  Serial.begin(115200);
  Serial.print("Connecting to.");
  Serial.printIn(ssid);

WiFi.mode(WiFi_STA);
  WiFi.begin(ssid password)
    while(WiFi.status() !=WL_CONNECTED)(
    delay(500)
    Serial.print(".."))
Serial.printIn("Nodemcu(esp8266)is connected to the ssid")
Serial.printIn(WiFi.localIP{});
  server.begin{};
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:
WiFiClient client;
client=server.available();

  if(client==1)(
    String request= client.readStringUntil('\n');
    client.flush();
    serial.printIn(request);
  if(request.Index("ledon") !=-1)(
    digitalWrite(led,HIGH);
    serial.printIn("LED IS ON NOW");)
  else if(request.indexOf("ledoff" !=-1))(
    digitalWrite(led,LOW);
    serial.printIn("LED IS ON NOW");)
    serial.print("Client Disconnected")
    serial.printIn(".........................................")
  Serial.printIn("                          ")
}
