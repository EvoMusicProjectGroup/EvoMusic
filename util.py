# class Note:
#     def __init__(self):
#         self.channel = 0
#         self.note = 0
#         self.velocity = 0
#         self.tick = 0
#         self.type = True
# 
# 
#     def __init__(self, channel, note, velocity, tick, note_type):
#         self.channel = channel
#         self.note = note
#         self.velocity = velocity
#         self.tick = tick
#         self.type = note_type
# 
#     def set_channel(self,channel):
#         self.channel = channel
# 
#     def set_note(self,note):
#         self.note = note
# 
#     def set_velocity(self,velocity):
#         self.velocity = velocity
# 
#     def set_tick(self,tick):
#         self.tick = tick
# 
#     def set_type(self,type):
#         self.type = type
# 
# 
#     def display(self):
#         print("Note", self.channel, self.note, self.velocity, self.tick)
from mido import Message, MetaMessage, MidiFile, MidiTrack
class Feature_pool:

  def __init__(self, pool=[]):
    self.feature_pool = pool

  def new_feature(self, notes):
    '''
    if it exists add to a feature if it not exist add it to a new feature object
    :param notes:  a list of note objects 
    :return: 
    '''
    name = [note.note for note in notes]
    # if note exist,add time to it or create a new note
    for item in self.feature_pool:
      if item.name == name:
        return item.add_phenotype(notes)
    # not exist , new note
    new_feature = Feature(notes)
    self.feature_pool.append(new_feature)

  def show_pool(self):
    for item in self.feature_pool:
      print('feature:', item.name, 'count:', item.count)

  def give_pool(self, min_count):
    pool_list = []
    for item in self.feature_pool:
      if item.count >= min_count:
        pool_list.append(item)
    return pool_list

class Feature:
  def __init__(self, notes):
    '''
    note is a list of note objects
    :param notes: 
    '''
    self.name = [note.note for note in notes]
    self.notes = notes
    self.phenotypes  = [notes]
    # self.duration =[[note.duration for note in notes]]
    # self.duration = notes
    self.count = 1

  def add_phenotype(self, notes):
    # add count if new add  to list if exist add to list
    duration = [note.duration for note in notes]
    if duration not in self.phenotypes:
      self.count += 1
      return self.phenotypes.append(notes)
    self.count += 1
    return self.phenotypes.append(notes)

  def get_time(self, time):
    return time in self.time

  def get_note(self):
    return self.note

class Note:
  def __init__(self):
    self.channel = 0
    self.note = [-1]
    self.velocity = 0
    self.start_time = 0
    self.duration = 0


  def __init__(self, channel, note, velocity, start_time, duration):
    '''
    with argument
    :param channel: 
    :param note: list[5,6] or [10] or [-1]
    :param velocity: 
    :param time: 
    :param note_type: 
    '''
    self.channel = channel
    self.note = note
    self.velocity = velocity
    self.start_time = start_time
    self.duration = duration

  def display(self):
    print("Note", self.channel, self.note, self.velocity, self.tick)

class Track:
    def __init__(self,feature_list=[]):
      self.feature_list = feature_list
      self.size = 0

    def feature_append(self, new_feature):
      self.feature_list.append(new_feature)
      self.size += 1

class Music:
    def __init__(self,track_list=[]):
      self.track_list = track_list
      self.ticks_per_beat = 100

    def set_ticks_per_beat(self, ticks_per_beat):
      self.ticks_per_beat = ticks_per_beat

    def append_track(self, new_track):
      self.track_list.append(new_track)

    def display(self):
      for i in range(len(self.track_list)):
        print("Track:", i)

        print("Note      :", end="")
        for j in range(len(self.track_list[i].feature_list)):
          for k in self.track_list[i].feature_list[j]:
            for z in k:
              print(z.note, end=' ')
            print(" | ",end='')
        print("")

        print("Duration  :", end="")
        for j in range(len(self.track_list[i].feature_list)):
            for k in self.track_list[i].feature_list[j]:
                for z in k:
                    print(z.duration, end=' ')
                print(" | ", end='')
        print("")


        print("")



    def save_midi(self,save_path = 'new_song.mid'):
        mid = MidiFile()
        for track_index in range(len(self.track_list)):

            track = MidiTrack()
            mid.tracks.append(track)
            # track.append(Message('program_change', program=12, time=0))
            for feature_index in range(self.track_list[track_index].size):
                # print("有track",track_index)
                for note in self.track_list[track_index].feature_list[feature_index]:
                    print("hahaha",note_note)
                    velocity = note.velocity
                    note_note = note.note
                    start_time = note.start_time
                    duration = note.duration
                    channel = note.channel
                    for i in note_note:
                        track.append(Message('note_on', channel=channel, note=i, velocity=velocity, time=0))
                    gap = duration
                    for i in note_note:
                        track.append(Message('note_off', channel=channel, note=i, velocity=velocity, time=gap))
                        gap = 0
        track.append(MetaMessage('end_of_track', time=0))
        mid.ticks_per_beat=self.ticks_per_beat
        mid.save(save_path)



if __name__ == "__main__":
    pass