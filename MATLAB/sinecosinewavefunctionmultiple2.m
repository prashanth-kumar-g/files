t=0:0.1:2*pi;
a=sin(t);
b=cos(t);

subplot(2,1,1)
plot(t, a, 'r<-', 'MarkerSize', 2, 'LineWidth', 2)
grid on
xlabel('Time', 'FontSize', 10)
ylabel('Amplitude', 'FontSize', 10)
title('sinewave function', 'FontSize', 16)
legend('cosinewave', 'Location', 'best')

subplot(2,1,2)
plot(t, b, 'b<-', 'MarkerSize', 2, 'LineWidth', 2)
grid on
xlabel('Time', 'FontSize', 10)
ylabel('Amplitude', 'FontSize', 10)
title('cosinewave function', 'FontSize', 16)
legend('sinewave', 'Location', 'best')