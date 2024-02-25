import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Rectangle;

public class Square implements Drawable, DrawableASCII {
   private int sideLength;

   public Square(int sideLength) {
      this.sideLength = sideLength;
   }

   @Override
   public void draw(Graphics2D graphicsObject) {
      Rectangle shapeObject = new Rectangle(0, 0, this.sideLength, this.sideLength);
      Color colorObject = new Color(255, 0, 0);
      graphicsObject.setColor(colorObject);
      graphicsObject.fill(shapeObject);
   }

   @Override
   public void drawASCII(char drawChar) {
      int rowIndex;
      int columnIndex;

      for (rowIndex = 0; rowIndex < this.sideLength; ++rowIndex) {
         for (columnIndex = 0; columnIndex < this.sideLength; ++columnIndex) {
            System.out.print(drawChar);
         }
         System.out.println();
      }
   }
}

