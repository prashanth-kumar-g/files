t=0:0.1:2*pi;
a=sin(t);
plot(t, a, 'r<-', 'MarkerSize', 2, 'LineWidth', 2)
grid on
xlabel('Time', 'FontSize', 10)
ylabel('Amplitude', 'FontSize', 10)
title('sinewave function', 'FontSize', 16)
legend('sinewave')
text(1, 0, 'Theta is 90')