from ai_utils import get_response

content = "0:0:0.0 --> 0:0:0.870Tiffany BouchardYeah, hopefully.0:0:4.560 --> 0:0:5.180Jialin ShanSo.0:0:6.90 --> 0:0:6.500Tiffany BouchardHello.0:0:7.360 --> 0:0:7.760Jialin ShanHello.0:0:12.140 --> 0:0:12.610Jialin ShanAlright.0:0:15.850 --> 0:0:18.950Jialin ShanSo it will just.0:0:20.900 --> 0:0:21.830Jialin ShanGet the bot.0:0:25.520 --> 0:0:30.390Jialin ShanTo record it after if we end the meeting at some point.0:0:30.990 --> 0:0:34.230Tiffany BouchardYeah, apparently. Can you see the transcription on the side?0:0:35.480 --> 0:0:40.590Jialin ShanUh, let me see. Transcript. Yeah, I can see it.0:0:42.210 --> 0:0:42.620Tiffany BouchardCool.0:0:43.540 --> 0:0:45.730Jialin ShanYeah. Nice. Nice. Nice, nice, nice.0:0:49.170 --> 0:0:54.240Tiffany BouchardI find that if you're not like super clear and like you went on tape properly, it actually like.0:0:54.930 --> 0:0:56.80Tiffany BouchardDoesn't know what you're saying.0:0:58.90 --> 0:0:58.360Tiffany BouchardYeah.0:0:57.420 --> 0:0:59.990Jialin ShanYeah, I think the nice part about it is that.0:1:3.400 --> 0:1:6.560Jialin ShanLike if you want to plug plug it into the chat JPL.0:1:7.360 --> 0:1:10.560Jialin ShanThe IT will figure it out, so that's the nice part cause.0:1:12.420 --> 0:1:13.250Tiffany BouchardOh yeah, for sure.0:1:19.390 --> 0:1:19.840Tiffany BouchardUmm.0:1:12.930 --> 0:1:23.610Jialin ShanI I I try plugging in some of the ones that Alana found and they had a little bit of weird transcription errors from.0:1:25.70 --> 0:1:27.40Jialin ShanTeams itself, and I figured it out.0:1:27.820 --> 0:1:31.90Tiffany BouchardOK, that's really good. Should we leave it and see?0:1:35.480 --> 0:1:35.920Tiffany BouchardOK.0:1:34.230 --> 0:1:37.830Jialin ShanYeah, let's see if it gives it out and then we'll.0:1:38.630 --> 0:1:43.250Jialin ShanWe can use this as example of a meeting note too so.0:1:43.940 --> 0:1:44.560Tiffany BouchardSounds good.0:1:46.130 --> 0:1:47.800Jialin ShanOK. Bye bye.0:1:48.560 --> 0:1:49.50Tiffany BouchardBy."

prompt_categories = [
    # {"title": "", "prompt": "\nList speakers in the meeting. \nList Agenda discussed in the meeting. \nList the resolutions reached in the meeting. \nList next Steps\n"},

    {"title": "\nSpeakers:", "prompt": "\nList speakers in the meeting\nSpeakers:\n-"},
    {"title": "\nAgenda items:", "prompt": "\nList the Agenda of the meeting\nAgenda items:\n-"},
    {"title": "\nResolutions:", "prompt": "\nList conclusions reached in the meeting\nConclusions:\n-"},
    {"title": "\nNext Steps:", "prompt": "\nWhat is next after the meeting\nNext Steps:\n-"}
]

# Prompt postfix
prompt_postfix = """ <document>
  \n###
"""
#print(prompt_postfix)


for prompt in prompt_categories:
    print(prompt["title"])
    prompt_with_postfix = prompt_postfix + prompt["prompt"]
    response = get_response(content, prompt_with_postfix)
    print("-" + response)
