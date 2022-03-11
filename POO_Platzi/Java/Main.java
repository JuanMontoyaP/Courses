class Main {
    public static void main(String[] args) {
        System.out.println("Hello World");

        UberX uberX = new UberX("AMQ123", new Driver("Juan", "123"), "Tesla", "X");
        uberX.setPassenger(4);
        uberX.printDataCar();

        UberVan uberVan = new UberVan("FHG456", new Driver("JP", "456"));
        uberVan.setPassenger(6);
        uberVan.printDataCar();
    }

}