channelID = 2854252;  
fieldID = 1;  
readAPIKey = 'N1W143XNQIVEO2NN'; 

numPoints = 10; 
data = thingSpeakRead(channelID, 'NumPoints', numPoints, 'Fields', fieldID, 'ReadKey', readAPIKey);

if ~isempty(data)
    avgTemp = mean(data); 
    disp(['Promedio de los últimos 10 datos: ', num2str(avgTemp), ' °C']);
else
    disp('No hay suficientes datos para calcular el promedio.');
end
