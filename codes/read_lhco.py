def read_lhco(name, nmax = None, OutputType = 'array'):
    with open(name) as fp:
        Lines     = fp.readlines()
        #print(len(Lines))
        variables = Lines[0].strip().split()
        nevents   = 0
        events    = []
        flag      = 0
        if OutputType == 'array':
            events = []
            ev_num = 0
            for line in Lines[1:]:
                aux = [float(x) for x in line.strip().split()]
                particle_props = np.zeros(12)
                if aux[0] == 0: # New event
                    ev_num = ev_num + 1
                else:
                    particle_props[0] = int(ev_num - 1) # Just to have the same number as the lhco
                    particle_props[1:] = np.asarray(aux)
                    events.append(particle_props)
            events = np.asarray(events)
            
        if OutputType == 'df':
            events = []
            ev_num = 0
            for line in Lines[1:]:
                aux = [float(x) for x in line.strip().split()]
                particle_props = np.zeros(12)
                if aux[0] == 0: # New event
                    ev_num = ev_num + 1
                else:
                    particle_props[0] = int(ev_num - 1) # Just to have the same number as the lhco
                    particle_props[1:] = np.asarray(aux)
                    events.append(particle_props)
            events = np.asarray(events)
            events = pd.DataFrame(data = events, columns = ['evNum'] + variables)
                
        if OutputType == 'dict':
            for line in Lines[1:]:
                aux = [float(x) for x in line.strip().split()]
                #print(aux)
                if aux[0] == 0: 
                    if flag == 1: # This means that we have to save the previous event
                        event_aux_dict = {'photon' : photon_aux_list, 
                                          'electron' : electron_aux_list, 
                                          'muon' : muon_aux_list, 
                                          'tau' : tau_aux_list, 
                                          'jet' : jet_aux_list, 
                                          'met' : met_aux_list 
                                         }
                        events.append( event_aux_dict )
                        if nevents == nmax: break


                    nevents = nevents + 1 # Event counter

                    # Initialize all event type list
                    photon_aux_list   = []
                    electron_aux_list = []
                    muon_aux_list     = []
                    tau_aux_list      = []
                    jet_aux_list      = []
                    met_aux_list      = []
                    # ---------------------------------

                if aux[0] > 0: # This means that there is a particle
                    flag = 1
                    # Let's read the properties and create the particle dictionary
                    aux_dict = {}
                    for i, ival in enumerate(aux[2:]):
                        aux_dict.setdefault(variables[i + 2], ival)
                    # ------------------------------------------------------------

                    # Let's save the dictionary in the corresponding list    
                    if aux[1] == 0: photon_aux_list.append(aux_dict) # Typ 0 is a photon
                    if aux[1] == 1: electron_aux_list.append(aux_dict) # Typ 1 is a electron
                    if aux[1] == 2: muon_aux_list.append(aux_dict) # Typ 2 is a muon
                    if aux[1] == 3: tau_aux_list.append(aux_dict) # Typ 3 is a tau    
                    if aux[1] == 4: jet_aux_list.append(aux_dict) # Typ 4 is a jet
                    if aux[1] == 6: met_aux_list.append(aux_dict) # Typ 6 is a met
                    # --------------------------------------------------------
            if flag == 1: # Save the last event
                event_aux_dict = {'photon' : photon_aux_list, 
                                  'electron' : electron_aux_list, 
                                  'muon' : muon_aux_list, 
                                  'tau' : tau_aux_list, 
                                  'jet' : jet_aux_list, 
                                  'met' : met_aux_list 
                                 }
                events.append( event_aux_dict )
    return events