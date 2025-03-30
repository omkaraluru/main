import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class LoginFrame extends JFrame implements ActionListener {
    JLabel l1, l2, background;
    JTextField tf1;
    JPasswordField pf;
    JButton btn1, btn2;

    LoginFrame() {
        setTitle("Restaurant Management System - Login");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 150);
        setResizable(true);
        setLocationRelativeTo(null);

        l1 = new JLabel("Username:");
        l2 = new JLabel("Password:");
        tf1 = new JTextField(10);
        pf = new JPasswordField(10);
        btn1 = new JButton("Login");
        btn2 = new JButton("Reset");

        JPanel p1 = new JPanel(new GridLayout(2, 1));
        JPanel p2 = new JPanel(new GridLayout(2, 1));
        JPanel p3 = new JPanel(new FlowLayout());

        p1.setOpaque(false);
        p2.setOpaque(false);
        p3.setOpaque(false);

        p1.add(l1);
        p1.add(l2);

        p2.add(tf1);
        p2.add(pf);

        p3.add(btn1);
        p3.add(btn2);

        setLayout(new BorderLayout());
        add(p1, BorderLayout.WEST);
        add(p2, BorderLayout.CENTER);
        add(p3, BorderLayout.SOUTH);

        getRootPane().setDefaultButton(btn1);

        btn1.addActionListener(this);
        btn2.addActionListener(this);
    }

    public void actionPerformed(ActionEvent ae) {
        if (ae.getSource() == btn1) {
            String uname = tf1.getText();
            String pass = new String(pf.getPassword());

            if (uname.equals("Omkar") && pass.equals("1212")) {
                JOptionPane.showMessageDialog(this, "Login successful!");
                dispose();
                new MenuFrame().setVisible(true);
            } else {
                JOptionPane.showMessageDialog(this, "Invalid username or password!");
            }
        } else if (ae.getSource() == btn2) {
            tf1.setText("");
            pf.setText("");
        }
    }

    public static void main(String[] args) {
        new LoginFrame().setVisible(true);
    }
}
