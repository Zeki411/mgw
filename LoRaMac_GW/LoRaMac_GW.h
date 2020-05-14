#ifndef LORA_MAC_GW_H
#define LORA_MAC_GW_H

#ifdef __cplusplus
extern "C" {
#endif
	
#include "./LoRaMac_GW_Types.h"
#include "./cfg/LoRaMac_GW_Cfg.h"

/*!
 * Parse a serialized data message and fills the structured object.
 *
 * \param[IN/OUT] macMsg       - Data message object
 * \retval                     - Status of the operation
 */
LoRaMacParserStatus_t LoRaMac_ParserData( LoRaMacMessageData_t *macMsg );

LoRaMacSerializerStatus_t LoRaMac_SerializePacket(LoRaMacMessageData_t *mac_msg);

void LoRaMac_SetACKPacket(LoRaMacMessageData_t *mac_msg);

#ifdef __cplusplus
}
#endif

#endif /* LORA_MAC_GW_H */
