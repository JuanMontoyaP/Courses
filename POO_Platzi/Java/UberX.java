class UberX extends Car {
    String brand;
    String model;

    public UberX(String license, Driver driver, String brand, String model) {
        super(license, driver);
        this.brand = brand;
        this.model = model;
    }

    @Override
    void printDataCar() {
        super.printDataCar();
        System.out.println("model: "+ model+ " Brand: " + brand);
    }
}
