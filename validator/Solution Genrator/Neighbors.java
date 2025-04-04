/**
 *
 * @author NAME
 */

import java.awt.Point;
import java.util.*;
import java.io.*;
import java.lang.*;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.*;


public class Neighbors {
    public static void main(String[] args) throws Exception {
        JSONParser parser = new JSONParser();
        ArrayList<Point> points=new ArrayList<Point>();
      try {
         Object obj = parser.parse(new FileReader("Neighborhood_100000_1000x1000.json"));
         JSONObject jsonObject = (JSONObject)obj;
         String name = (String)jsonObject.get("name");
         JSONArray pairs = (JSONArray)jsonObject.get("pairList");
          //System.out.println(name);
          for (Object pair : pairs) {
              JSONArray p=(JSONArray)pair;
              //System.out.println(p);
              points.add(new Point(((java.lang.Long)(p.get(0))).intValue(),
              ((java.lang.Long)(p.get(1))).intValue()));
              
              //System.out.println(p.get(1).getClass());
              //System.out.println(pair.getClass());
              
          }
      } catch(Exception e) {
         e.printStackTrace();
      }
        System.out.println(points);
        ArrayList<Location> spots=new ArrayList<Location>();
        for (Point point : points) {
            spots.add(new Location(point.x, point.y, points));
//            System.out.println("===========");
        }
        
        JSONObject j2 = new JSONObject();
       // j2.put("name", "Nearest Points");
        JSONArray orders=new JSONArray();
        for (Location spot : spots) {
            JSONObject j3=new JSONObject();
            j3.put("location", spot.getMyLocationJSON());
            j3.put("closestPoint", spot.bestOne());
            orders.add(j3);
        }
        j2.put("allLocations", orders);
        //System.out.println(j2.toJSONString());
        
        try (FileWriter file = new FileWriter("output.json")) {
         file.write(j2.toJSONString());
         System.out.println("JSON Object write to a File successfully");
         //System.out.println("JSON Object: " + obj);
      }
   }
    
    
}




/*
import java.io.*;
import java.util.*;
import org.json.simple.*;
import org.json.simple.parser.*;
public class JSONObjectWriterToFileTest {
   public static void main(String[] args) throws IOException {
      JSONObject obj = new JSONObject();
      obj.put("Name", "Adithya");
      obj.put("Course", "MCA");
      JSONArray subjects = new JSONArray();
      subjects.add("Subject1: DBMS");
      subjects.add("Subject2: JAVA");
      subjects.add("Subject3: PYTHON");
      obj.put("Subjects:", subjects);
      try (FileWriter file = new FileWriter("/Users/User/Desktop/course1.json")) {
         file.write(obj.toJSONString());
         System.out.println("JSON Object write to a File successfully");
         System.out.println("JSON Object: " + obj);
      }
   }
}

*/