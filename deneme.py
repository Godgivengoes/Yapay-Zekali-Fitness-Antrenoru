renk1 = (0, 255, 0)
                if per4 == 100:
                    renk1 = (255, 0, 255)
                if aci3 > 160:
                    stage = 'down'
                    print(stage)
                if per4 == 0:
                    renk1 == (0, 255, 255)
                if aci3 < 100 and stage == 'down':
                    stage = 'up'
                    print(stage)
                    say3 += 1
                    print(say3)


                if stage=="up":
                    per4=100
                    renk1 = (255, 0, 255)

                elif stage=="down":
                    per4=0
                    renk1 = (0, 255, 0)
