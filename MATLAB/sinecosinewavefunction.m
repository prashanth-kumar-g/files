t=0:0.1:2*pi;
a=sin(t);
b=cos(t);
hold on
plot(t, a, 'r<-', 'MarkerSize', 2, 'LineWidth', 2)
plot(t, b, 'b<-', 'MarkerSize', 2, 'LineWidth', 2)
grid on
xlabel('Time', 'FontSize', 10)
ylabel('Amplitude', 'FontSize', 10)
title('sine-cosine wave function', 'FontSize', 16)
legend('sinewave', 'cosinewave', 'Location', 'best')
