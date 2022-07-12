function ef = bandpassdesig_mode_gg(efs, y, wp, ws, rp, rs,n)
% band模拟滤波器
% 处理前 + 频响函数 + 处理后
%xx=sin(2*pi*18000*t)+sin(2*pi*1000*t)
%% efs= frequncy; ex= signal;
sigLength=length(y);
t=0:1/efs:(sigLength-1)/efs;
[freq amp] = myfft(y, efs);
if n
%subplot(321);
plot(freq, amp);xlim([0,100])
xlabel('Frequency (Hz)'); title('Before fiter');
ylabel('|Y(f)|');
end
[N, Wn] = buttord(wp* 2 / efs, ws* 2 / efs, rp, rs);
[Fb,Fa]=butter(N, Wn); 
[h,w]=freqz(Fb,Fa);%求滤波器参数

if n-1
subplot(322); plot(w/pi*efs/2,abs(h)); grid on;xlim([0,100]);
xlabel('Frequency(Hz)'); ylabel('Magnitude(DB)'); title('Frequency Response');
%set_fig_fontsize(12);
end

ef = filtfilt(Fb, Fa, y);%滤波
if n
 %plot(t,y); title('original');xlabel('Time(s)');ylabel('Voltage(V)');
subplot(321); plot(t,ef); title('filter'); xlabel('Time(s)');ylabel('Voltage(V)');hold on;
end
[freq amp] = myfft(ef, efs);
if n
%plot(freq/1, amp);
xlim([0,10]);
xlabel('Frequency (Hz)');%xlim([0 220000]);
%subplot(322);ylabel('|Y(f)|');title('After fiter');
end
end
%subplot(311); plot(t,x); ylabel('original')
%subplot(312); plot(t,xf);  ylabel('filter')
%subplot(313); plot(t,xh);
