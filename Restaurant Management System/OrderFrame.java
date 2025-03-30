import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class OrderFrame extends JFrame implements ActionListener {
    JLabel l1, l2, l3, l4, l5;
    JButton btn1, btn2;
    JComboBox<String> comboBox;
    JComboBox<Integer> qtyComboBox;

    String[] itemNames = { "Milk", "Tea", "Coffee", "Idly", "Dosa", "Ghee Karam Podi Idly", "Sambar Button Idly",
            "Vada With Chicken Curry", "Veg Noodles", "Chicken Noodles", "Gravy Chicken Noodles",
            "Poori with Chicken Curry", "Poori With Aloo Curry", "Chicken Fry", "Chicken Curry", "Paya Roti",
            "Tawa Paneer", "Veg biryani", "Hyderbad di Dum biryani", "Spl Chicken Dum biryani", "North Indian thali",
            "South Indian thali", "Cool Drinks" };

    double[] itemPrices = { 20.0, 10.0, 15.0, 40.0, 40.0, 50.0, 35.0, 80.0, 90.0, 120.0, 130.0, 90.0, 70.0, 200.0,
            150.0, 120.0, 120.0,
            100.0, 180.0, 200.0, 200.0, 100.0, 20.0 };

    OrderFrame() {
        setTitle("Restaurant Management System - Order Food");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 200);
        setResizable(true);
        setLocationRelativeTo(null);

        l1 = new JLabel("Select item:");
        l2 = new JLabel("Select quantity:");
        l3 = new JLabel(" ");
        l4 = new JLabel(" ");
        l5 = new JLabel("Total Price: ₹0.00");

        btn1 = new JButton("View");
        btn2 = new JButton("Pay");

        comboBox = new JComboBox<>(itemNames);
        qtyComboBox = new JComboBox<>(new Integer[] { 1, 2, 3 });

        JPanel p1 = new JPanel(new GridLayout(2, 1));
        JPanel p2 = new JPanel(new GridLayout(2, 1));
        JPanel p3 = new JPanel(new GridLayout(2, 1));
        JPanel p4 = new JPanel(new FlowLayout());
        JPanel p5 = new JPanel(new GridLayout(2, 1));

        p1.add(l1);
        p1.add(l2);

        p2.add(comboBox);
        p2.add(qtyComboBox);

        p3.add(btn1);
        p3.add(btn2);

        p4.add(l3);
        p4.add(l4);

        // p5.add(new JLabel("Item price: "));
        p5.add(l5);

        setLayout(new BorderLayout());
        add(p1, BorderLayout.WEST);
        add(p2, BorderLayout.CENTER);
        add(p3, BorderLayout.EAST);
        add(p4, BorderLayout.SOUTH);
        add(p5, BorderLayout.NORTH);

        btn1.addActionListener(this);
        btn2.addActionListener(this);
    }

    public void actionPerformed(ActionEvent ae) {
        if (ae.getSource() == btn1) {
            String item = (String) comboBox.getSelectedItem();
            int qty = (int) qtyComboBox.getSelectedItem();
            double itemPrice = itemPrices[comboBox.getSelectedIndex()];
            double totalPrice = qty * itemPrice;

            l3.setText("Item added: " + item + " (Quantity: " + qty + ")");
            l4.setText(String.format("Total price for this item: ₹%.2f", totalPrice));
            double currentTotal = Double.parseDouble(l5.getText().substring(14));
            double newTotal = currentTotal + totalPrice;
            l5.setText(String.format("Total Price: ₹%.2f", newTotal));
        } else if (ae.getSource() == btn2) {
            PaymentFrame paymentFrame = new PaymentFrame();
            paymentFrame.setVisible(true);
        }
    }

    public static void main(String[] args) {
        new OrderFrame().setVisible(true);
    }
}
