
import java.awt.Point;
import java.util.ArrayList;
import org.json.simple.JSONArray;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/**
 *
 * @author jbarrett
 */
public class Location {

    Point myLocation;
    ArrayList<Point> allPoints, myPoints;

    public Location(int x1, int y1, ArrayList<Point> allP) {
        myLocation = new Point(x1, y1);
        allPoints = allP;
        myPoints = new ArrayList<Point>();
        for (Point allPoint : allPoints) {
            addPossiblePoint(allPoint);
        }
        //System.out.println(myLocation);
//        for (Point myPoint : myPoints) {
//            System.out.println(myPoint);
//        }
    }

    public void printLastLocation() {
        System.out.println(allPoints.get(allPoints.size() - 1));
    }

    public void addPossiblePoint(Point p) {
        if (!myLocation.equals(p) && !myPoints.contains(p)) {
            myPoints.add(p);
        }
        while (myPoints.size() > 3) {
            double d0 = myLocation.distance(myPoints.get(0));
            double d1 = myLocation.distance(myPoints.get(1));
            double d2 = myLocation.distance(myPoints.get(2));
            double d3 = myLocation.distance(myPoints.get(3));
            if (d0 >= d1 && d0 >= d2 && d0 >= d3) {
                myPoints.remove(0);
            } else if (d1 > d2 && d1 > d3) {
                myPoints.remove(1);
            } else if (d2 > d3) {
                myPoints.remove(2);
            } else {
                myPoints.remove(3);
            }

        }
    }

    public JSONArray getMyLocationJSON() {
        JSONArray me = new JSONArray();
        me.add(myLocation.x);
        me.add(myLocation.y);
        return me;
    }

    public JSONArray bestThree() {
        JSONArray best3 = new JSONArray();
        for (Point myPoint : myPoints) {
            JSONArray you = new JSONArray();
            you.add(myPoint.x);
            you.add(myPoint.y);
            best3.add(you);
        }
        return best3;
    }

    public JSONArray bestOne() {
        double d0 = myLocation.distance(myPoints.get(0));
        double d1 = myLocation.distance(myPoints.get(1));
        double d2 = myLocation.distance(myPoints.get(2));
        int selected = -1;
        if (d0 < d1 && d0 < d2) {
            selected = 0;
        } else if (d1 > d2) {
            selected = 1;
        } else {
            selected = 2;
        }

        Point myPoint = myPoints.get(selected);

        JSONArray you = new JSONArray();
        you.add(myPoint.x);
        you.add(myPoint.y);
        
        return you;
    }
}
