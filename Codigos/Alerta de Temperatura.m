channelID = 2854252;  
fieldID = 1;  
readAPIKey = 'N1W143XNQIVEO2NN'; 

data = thingSpeakRead(channelID, 'NumPoints', 1, 'Fields', fieldID, 'ReadKey', readAPIKey);

if ~isempty(data)
    currentTemp = data(1);
    disp(['Temperatura actual: ', num2str(currentTemp), ' °C']);
    
    if currentTemp > 35
        disp('⚠️ ALERTA: Temperatura alta (> 35°C) ⚠️');
    end
else
    disp('No se pudo obtener la temperatura actual.');
end