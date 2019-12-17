from typing import List, Optional, Union
from pyyoutube.models import PlaylistItemListResponse
from pyyoutube.utils.params_checker import enf_parts


def get_playlist_all_items(
    api,
    *,
    playlist_id: str,
    parts: Optional[Union[str, list, tuple, set]] = None,
    video_id: Optional[str] = None,
    count: Optional[int] = 5,
    return_json: Optional[bool] = False,
):
    """
    Retrieve all playlist Items info by your given playlist id

    Args:
        playlist_id (str):
            The id for playlist that you want to retrieve items data.
        parts ((str,list,tuple,set) optional):
            The resource parts for you want to retrieve.
            If not provide, use default public parts.
            You can pass this with single part str, comma-separated parts str or a list,tuple,
            set of parts.
        video_id (str, Optional):
            Specifies that the request should return only the playlist items that contain the
            specified video.
        count (int, optional):
            Control how many items per page will be retreived.
            Default is 5.
        return_json(bool, optional):
            The return data type. If you set True JSON data will be returned.
            False will return a pyyoutube.PlayListItemApiResponse instance.
    Returns:
        PlaylistItemListResponse or original data
    """
    args = {
        "playlistId": playlist_id,
        "part": enf_parts(resource="playlistItems", value=parts),
        "maxResults": count,
    }
    if video_id is not None:
        args["video_id"] = video_id

    res_data: Optional[dict] = None
    current_items: List[dict] = []
    next_page_token: Optional[str] = None
    while True:
        prev_page_token, next_page_token, data = api.paged_by_page_token(
            resource="playlistItems", args=args, page_token=next_page_token
        )
        items = api._parse_data(data)
        current_items.extend(items)
        if res_data is None:
            res_data = data
        if next_page_token is None:
            break

    res_data["items"] = current_items
    if not return_json:
        res_data = PlaylistItemListResponse.from_dict(res_data)
    return res_data
