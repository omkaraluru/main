import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class MenuFrame extends JFrame implements ActionListener {
    JLabel l1, l2, l3, l4;
    JButton btn1, btn2;

    MenuFrame() {
        setTitle("Restaurant Management System - Menu");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 150);
        setResizable(true);
        setLocationRelativeTo(null);

        l1 = new JLabel("Select an option:");
        l2 = new JLabel(" ");
        l3 = new JLabel(" ");
        l4 = new JLabel(" ");

        btn1 = new JButton("Order Food");
        btn2 = new JButton("Logout");

        JPanel p1 = new JPanel(new GridLayout(2, 1));
        JPanel p2 = new JPanel(new GridLayout(2, 1));
        JPanel p3 = new JPanel(new GridLayout(2, 2));

        p1.add(l1);
        p1.add(l2);

        p2.add(l3);
        p2.add(l4);

        p3.add(btn1);
        p3.add(btn2);

        setLayout(new BorderLayout());
        add(p1, BorderLayout.NORTH);
        add(p2, BorderLayout.CENTER);
        add(p3, BorderLayout.SOUTH);

        getRootPane().setDefaultButton(btn1);

        btn1.addActionListener(this);
        btn2.addActionListener(this);
    }

    public void actionPerformed(ActionEvent ae) {
        if (ae.getSource() == btn1) {
            dispose();
            new OrderFrame().setVisible(true);
        } else if (ae.getSource() == btn2) {
            dispose();
            new LoginFrame().setVisible(true);
        }
    }

    public static void main(String[] args) {
        new MenuFrame().setVisible(true);
    }
}
