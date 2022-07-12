function [num_mean,T_mean,datacorrelation_mean] = knee_function(filepase)
    cd(filepase);
    addpath(genpath('..\'));
    number=1;
    for file=0:7
        %% 读取，滤波,归一化。得到四组滤波、归一化后信号。m:表格列数%%%%只需更改文件名和采样频率、m
        efs=250000;ymin=0;ymax=1;type=1;
        p=2;s=6;rp=5;rs=13.2;n=1;
        x1=linspace(0,4,1000000);
        filename=char('tek000'+string(file)+'ALL.csv');ef=zeros([1000000 4]);

        for m=1:3
            y=csvread(filename,21,m,[21,m,1000020,m]);
            ef=bandpassdesig_mode_gg(efs, y, p, s, rp, rs,n);
            em=guiyi(ef,type,ymin,ymax);

            %% 变点数num
            extrMaxValue=find(diff(sign(diff(em)))==-2)+1;
            extrMinValue=find(diff(sign(diff(em)))==2)+1;
            extrMaxValue_true=[];
            extrMinValue_true=[];
                for j=1:length(extrMaxValue)
                    num_var=0;
                    if extrMaxValue(j)<=10000
                        num_var=var(em((extrMaxValue(j):extrMaxValue(j)+20000)));
                    elseif extrMaxValue(j)>=990000
                        num_var=var(em((extrMaxValue(j)-20000:extrMaxValue(j))));
                    else
                        num_var=var(em((extrMaxValue(j)-10000:extrMaxValue(j)+10000)));
                    end
                    if num_var>9e-6
                        extrMaxValue_true(end+1)=extrMaxValue(j);
                    end
                end
                for k=1:length(extrMinValue)
                     num_var=0;
                    if extrMinValue(k)<=10000
                        num_var=var(em([extrMinValue(k):extrMinValue(k)+20000]));
                    elseif extrMinValue(k)>=990000
                        num_var=var(em([extrMinValue(k)-20000:extrMinValue(k)]));
                    else
                        num_var=var(em([extrMinValue(k)-10000:extrMinValue(k)+10000]));
                    end
                    if num_var>9e-6
                        extrMinValue_true(end+1)=extrMinValue(k);
                    end
                end
                num(file+1,m)=length(extrMaxValue_true)+length(extrMinValue_true);            
                %saveas(1,'save.jpg');
                %print 1.jpg -djpeg -r1000
                %hold off;
            %% 自相关系数ACF
                i=1;
                Max1=[];
                Max2=[];
                for j=1:length(extrMaxValue)
                        Max1(j)=em(extrMaxValue(j),i);
                        Max2(j)=Max1(j);
                    end
                try
                    [max1,place1]=max(Max1);
                    Max1(place1)=0;
                    [max2,place2]=max(Max1);
                    Max1(place2)=0;
                    [max3,place3]=max(Max1);
                    place_1=[extrMaxValue(place1) extrMaxValue(place2) extrMaxValue(place3)];
                    T1=floor((max(place_1)-min(place_1))/2);
                    data1=em(1:T1+1,i);
                    data2=em((median(place_1)-min(place_1)):(median(place_1)-min(place_1)+T1),i);
                    datacorrelation1=corr2(data1,data2);
                    data3=em(1000000-T1:1000000,i);
                    data4=em((median(place_1)+1000000-max(place_1)-T1):(median(place_1)+1000000-max(place_1)),i);
                    datacorrelation2=corr2(data3,data4);
                    datacorrelation_1=(datacorrelation1+datacorrelation2)/2;
                catch
                    T1=1;
                    datacorrelation_1=0;
                end

                [max4,place4]=max(Max2);
                Max2(place4)=0;
                [max5,place5]=max(Max2);
                Max2(place5)=0;
                [max6,place6]=max(Max2);
                Max2(place6)=0;
                [max7,place7]=max(Max2);
                place_prepare=[extrMaxValue(place4) extrMaxValue(place5) extrMaxValue(place6) extrMaxValue(place7)];
                place_2_prepare=sort(place_prepare);
                place_2=place_2_prepare(1:3);
                place_3=place_2_prepare(2:4);

                try
                    T2=floor((max(place_2)-min(place_2))/2);
                    data5=em(1:T2+1,i);
                    data6=em((median(place_2)-min(place_2)):(median(place_2)-min(place_2)+T2),i);
                    datacorrelation3=corr2(data5,data6);
                    data7=em(1000000-T2:1000000,i);
                    data8=em((median(place_2)+1000000-max(place_2)-T2):(median(place_2)+1000000-max(place_2)),i);
                    datacorrelation4=corr2(data7,data8);
                    datacorrelation_2=(datacorrelation3+datacorrelation4)/2;
                catch
                    T2=1;
                    datacorrelation_2=0;   
                end
                try
                    T3=floor((max(place_3)-min(place_3))/2);
                    data9=em(1:T3+1,i);
                    data10=em((median(place_3)-min(place_3)):(median(place_3)-min(place_3)+T3),i);
                    datacorrelation5=corr2(data9,data10);
                    data11=em(1000000-T3:1000000,i);
                    data12=em((median(place_3)+1000000-max(place_3)-T3):(median(place_3)+1000000-max(place_3)),i);
                    datacorrelation6=corr2(data11,data12);
                    datacorrelation_3=(datacorrelation5+datacorrelation6)/2;
                catch
                    T3=1;
                    datacorrelation_3=0;   
                end
                Min1=[];
                Min2=[];
                for j=1:length(extrMinValue)
                        Min1(j)=em(extrMinValue(j),i);
                        Min2(j)=Min1(j);
                    end
                try
                    [max1,place1]=min(Min1);
                    Min1(place1)=1;
                    [max2,place2]=min(Min1);
                    Min1(place2)=1;
                    [max3,place3]=min(Min1);
                    minplace_1=[extrMinValue(place1) extrMinValue(place2) extrMinValue(place3)];
                    T4=floor((max(minplace_1)-min(minplace_1))/2);
                    data13=em(1:T4+1,i);
                    data14=em((median(minplace_1)-min(minplace_1)):(median(minplace_1)-min(minplace_1)+T4),i);
                    datacorrelation7=corr2(data13,data14);
                    data15=em(1000000-T4:1000000,i);
                    data16=em((median(minplace_1)+1000000-max(minplace_1)-T4):(median(minplace_1)+1000000-max(minplace_1)),i);
                    datacorrelation8=corr2(data15,data16);
                    mindatacorrelation_1=(datacorrelation7+datacorrelation8)/2;
                catch
                    T4=1;
                    mindatacorrelation_1=0;
                end

                [max4,place4]=min(Min2);
                Min2(place4)=1;
                [max5,place5]=min(Min2);
                Min2(place5)=1;
                [max6,place6]=min(Min2);
                Min2(place6)=1;
                [max7,place7]=min(Min2);
                minplace_prepare=[extrMinValue(place4) extrMinValue(place5) extrMinValue(place6) extrMinValue(place7)];
                minplace_2_prepare=sort(minplace_prepare);
                minplace_2=minplace_2_prepare(1:3);
                minplace_3=minplace_2_prepare(2:4);

                try
                    T5=floor((max(minplace_2)-min(minplace_2))/2);
                    data17=em(1:T5+1,i);
                    data18=em((median(minplace_2)-min(minplace_2)):(median(minplace_2)-min(minplace_2)+T5),i);
                    datacorrelation9=corr2(data17,data18);
                    data19=em(1000000-T5:1000000,i);
                    data20=em((median(minplace_2)+1000000-max(minplace_2)-T5):(median(minplace_2)+1000000-max(minplace_2)),i);
                    datacorrelation10=corr2(data19,data20);
                    mindatacorrelation_2=(datacorrelation9+datacorrelation10)/2;
                catch
                    T5=1;
                    mindatacorrelation_2=0;   
                end
                try
                    T6=floor((max(minplace_3)-min(minplace_3))/2);
                    data21=em(1:T6+1,i);
                    data22=em((median(minplace_3)-min(minplace_3)):(median(minplace_3)-min(minplace_3)+T6),i);
                    datacorrelation11=corr2(data21,data22);
                    data23=em(1000000-T6:1000000,i);
                    data24=em((median(minplace_3)+1000000-max(minplace_3)-T6):(median(mminplace_3)+1000000-max(minplace_3)),i);
                    datacorrelation12=corr2(data23,data24);
                    mindatacorrelation_3=(datacorrelation11+datacorrelation12)/2;
                catch
                    T6=1;
                    mindatacorrelation_3=0;   
                end
                
                if max(mindatacorrelation_2,mindatacorrelation_3)<=0
                    mindatacorrelation_2=0;
                else
                    if mindatacorrelation_2<mindatacorrelation_3
                        T5=T6;
                        mindatacorrelation_2=mindatacorrelation_3;
                        data17=data21;data18=data22;data19=data23;data20=data24;
                    end
                end
                if mindatacorrelation_2<mindatacorrelation_1
                        T5=T4;
                        mindatacorrelation_2=mindatacorrelation_1;
                        data17=data13;data18=data14;data19=data15;data20=data16;
                end
                
                                   
                if max(datacorrelation_2,datacorrelation_3)<=0
                    datacorrelation_2=0;
                else  
                    if datacorrelation_2<datacorrelation_3
                        T2=T3;
                        datacorrelation_2=datacorrelation_3;
                        data5=data9;data6=data10;data7=data11;data8=data12;
                    end
                end
                                                                                         
                if datacorrelation_2<mindatacorrelation_2&&mindatacorrelation_2>0
                    T2=T5;
                    datacorrelation_2=mindatacorrelation_2;
                    data5=data17;data6=data18;data7=data19;data8=data20;
                end
                
                if datacorrelation_1>datacorrelation_2
                    t=linspace(0,T1/1000000*4,T1+1);
                    %subplot(323);plot(t,data1,t,data2);
                    %subplot(324);plot(t,data3,t,data4);
                    datacorrelation(file+1,m)=datacorrelation_1;
                    T(file+1,m)=T1;
                else
                     t=linspace(0,T2/1000000*4,T2+1);
                     %subplot(323);plot(t,data5,t,data6);
                     %subplot(324);plot(t,data7,t,data8);
                     T(file+1,m)=T2;
                     datacorrelation(file+1,m)=datacorrelation_2;
                end
               number=number+1;
               display(number);
        end
        end
num_mean=mean(num(:));
T_mean=mean(T(:));
datacorrelation_sort=sort(datacorrelation(:));
datacorrelation_mean=mean(datacorrelation(:));
datacorrelation_middle=datacorrelation_sort(12);
display(datacorrelation_middle);

for j=0:7
    for k=1:3
        if datacorrelation(j+1,k)==datacorrelation_middle
           filename=char('tek000'+string(j)+'ALL.csv');ef=zeros([1000000 4]); 
           y=csvread(filename,21,k,[21,k,1000020,k]);
           ef=bandpassdesig_mode_gg(efs, y, p, s, rp, rs,n);
           em=guiyi(ef,type,ymin,ymax);
           t=linspace(0,4,1000000);
           plot(t,em);
           saveas(gcf,'1.png');
        end
    end
end
end

