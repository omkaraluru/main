import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class PaymentFrame extends JFrame implements ActionListener {
    JLabel l1;
    JButton cashButton, cardButton, onlineButton;

    PaymentFrame() {
        setTitle("Payment Options");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 200);
        setResizable(true);
        setLocationRelativeTo(null);

        l1 = new JLabel("Please select your payment method:");

        cashButton = new JButton("Cash");
        cardButton = new JButton("Debit/Credit Card");
        onlineButton = new JButton("Online Payment");

        JPanel p1 = new JPanel(new GridLayout(1, 1));
        JPanel p2 = new JPanel(new GridLayout(1, 3));

        p1.add(l1);

        p2.add(cashButton);
        p2.add(cardButton);
        p2.add(onlineButton);

        setLayout(new BorderLayout());
        add(p1, BorderLayout.NORTH);
        add(p2, BorderLayout.CENTER);

        cashButton.addActionListener(this);
        cardButton.addActionListener(this);
        onlineButton.addActionListener(this);
    }

    public void actionPerformed(ActionEvent ae) {
        if (ae.getSource() == cashButton) {
            JOptionPane.showMessageDialog(null, "Thank you for your payment! Goodbye!");
            dispose();
        } else if (ae.getSource() == cardButton) {
            JOptionPane.showMessageDialog(null, "Please swipe or insert your card. Thank you!");
            dispose();
        } else if (ae.getSource() == onlineButton) {
            JFrame qrFrame = new JFrame();
            qrFrame.setTitle("Online Payment QR Code");
            qrFrame.setSize(400, 400);
            qrFrame.setLocationRelativeTo(null);
            JLabel qrLabel = new JLabel(new ImageIcon("Qr_Code.png"));
            qrFrame.add(qrLabel);

            // Add an exit button
            JButton exitButton = new JButton("Exit");
            exitButton.addActionListener(new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    qrFrame.dispose();
                }
            });
            JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
            buttonPanel.add(exitButton);
            qrFrame.add(buttonPanel, BorderLayout.SOUTH);

            qrFrame.setVisible(true);
            dispose();
        }
    }

    public static void main(String[] args) {
        new PaymentFrame().setVisible(true);
    }
}
