function [freq,amp] = myfft(y, efs)
A=replaceInf(y);
B = A(~isnan(A));
L = length(B);
NFFT = 2^nextpow2(L); % Next power of 2 from length of y
Y = fft(B,NFFT)/L;
freq = efs/2*linspace(0, 1, NFFT/2);
amp = 2*abs(Y(1:NFFT/2));
%plot(freq, amp);