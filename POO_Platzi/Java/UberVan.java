import java.util.ArrayList;
import java.util.Map;

class UberVan extends Car {
    Map<String, Map<String,Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterial; 

    public UberVan(String license, Driver driver) {
        super(license, driver);
        // this.typeCarAccepted = typeCarAccepted;
        // this.seatsMaterial = seatsMaterial;
    }
    
    @Override
    public void setPassenger(Integer passenger) {
        if (passenger == 6) {
            this.passenger = passenger;
        }
        else {
            System.out.println("You need to enter 6 passengers");
        }
    }
}
