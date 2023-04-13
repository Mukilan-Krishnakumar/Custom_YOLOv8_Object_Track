from ultralytics import YOLO
import supervision as sv
from supervision.video  import VideoSink, VideoInfo


START = sv.Point(904,0)
END = sv.Point(904,1080)

SOURCE_VIDEO_PATH = "../Assets/Elephants_Crossing.mp4"
TARGET_VIDEO_PATH = "../Assets/BoTSORT_Elephants_Crossing.mp4"


video_info = VideoInfo.from_video_path(SOURCE_VIDEO_PATH)

model = YOLO("../4_Custom_Train_YOLOv8/runs/detect/train2/weights/best.pt")

line_zone = sv.LineZone(start = START, end = END)
line_zone_annotator = sv.LineZoneAnnotator(
    thickness = 2,
    text_thickness = 1,
    text_scale = 0.5
)
box_annotator = sv.BoxAnnotator(
    thickness = 2,
    text_thickness = 1,
    text_scale = 0.5
)

with VideoSink(TARGET_VIDEO_PATH, video_info) as sink:
    for result in model.track(source = SOURCE_VIDEO_PATH, project = "/notebooks/", stream = True,agnostic_nms = True, tracker = "botsort.yaml"):
        frame = result.orig_img
        detections = sv.Detections.from_yolov8(result)
        if result.boxes.id is not None:
            detections.tracker_id = result.boxes.id.cpu().numpy().astype(int)
        labels = [
            f'#{tracker_id} {model.model.names[class_id]}{confidence:0.2f}'
            for _, confidence, class_id, tracker_id
            in detections 
        ]
    
        frame = box_annotator.annotate(scene = frame, detections = detections, labels = labels)
        line_zone.trigger(detections=detections)
        line_zone_annotator.annotate(frame=frame, line_counter=line_zone)
        sink.write_frame(frame)